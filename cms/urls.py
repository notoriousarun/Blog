from django.urls import path
from .views import Signup, PostIndex, UserPostList, TagIndexView

urlpatterns = [
    path('signup', Signup, name='signup'),
    path('', PostIndex.as_view(), name='blogposts'),
    path('tag/<str:slug>/', TagIndexView.as_view(), name='tagged'),
    path('dashboard/', UserPostList.as_view(), name='dashboard'),
]
