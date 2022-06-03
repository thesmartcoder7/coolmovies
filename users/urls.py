from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup', views.signup, name='users_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='movies/index.html'), name='users_logout'),
    path('update/', views.update, name='users_update')
]
