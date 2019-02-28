from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView
from cms.forms import SignUpForm
from taggit.models import Tag
from cms.models import BlogPost


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostIndex(TagMixin, ListView):
    template_name = 'cms/index.html'
    model = BlogPost
    paginate_by = '10'
    queryset = BlogPost.objects.all()
    context_object_name = 'blogposts'


class TagIndexView(TagMixin, ListView):
    template_name = 'cms/index.html'
    model = BlogPost
    paginate_by = '10'
    context_object_name = 'blogposts'

    def get_queryset(self):
        return BlogPost.objects.filter(tags__slug=self.kwargs.get('slug'))


class UserPostList(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'cms/dashboard.html'
    context_object_name = 'all_posts_by_user'

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)


class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = '__all__'
    success_url = '/dashboard'


class BlogPostDetail(DetailView):
    model = BlogPost
