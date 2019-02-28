from django.contrib import admin
from django import forms
from .models import BlogPost


class BlogPostAdminForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ['page_title', 'image', 'content',
                    'meta_title', 'meta_description', 'category', 'location']


admin.site.register(BlogPost, BlogPostAdmin)
