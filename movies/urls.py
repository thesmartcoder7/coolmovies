from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='movies_landing'),
    path('all', views.all, name='movies_home' ),
    path('movies', views.movies, name='movies_movies'),
    path('tv', views.tv, name='movies_tv')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
