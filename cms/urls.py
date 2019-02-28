from django.urls import path
import cms.views as cms_view

urlpatterns = [
    path('signup/', cms_view.Signup, name='signup'),
    path('', cms_view.PostIndex.as_view(), name='blogposts'),
    path('tag/<str:slug>/', cms_view.TagIndexView.as_view(), name='tagged'),
    path('dashboard/', cms_view.UserPostList.as_view(), name='dashboard'),
    path('create/',  cms_view.BlogPostCreate.as_view(), name="create")
]
