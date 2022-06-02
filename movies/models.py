from django.db import models

# Create your models here.
class Movie:
    def __init__(self, title, id, overview, poster_path, backdrop_path):
        self.name = title
        self.id = id
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster_path
        self.backdrop = 'https://image.tmdb.org/t/p/w1280/'+ backdrop_path


class Show:
   def __init__(self, name, id, overview, poster_path, backdrop_path):
        self.name = name
        self.id = id
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster_path
        self.backdrop = 'https://image.tmdb.org/t/p/w1280/'+ backdrop_path
