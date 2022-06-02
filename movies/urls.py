from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movies_landing'),
    path('content', views.movies, name='movies_home' )
]