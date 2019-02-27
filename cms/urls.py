from django.urls import path
from cms import views as cms_views

urlpatterns = [
    path('signup', cms_views.signup, name='signup'),
    path('', cms_views.home, name='home'),
    path('Dashboard/', cms_views.dashboard, name='Dashboard'),
]
