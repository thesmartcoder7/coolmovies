from django.db import models

class Movie:
    """
    Represents a movie.

    Attributes:
        name (str): The title of the movie.
        id (int): The ID of the movie.
        overview (str): An overview or description of the movie.
        poster (str): The URL of the movie's poster image.
        backdrop (str): The URL of the movie's backdrop image.
    """

    def __init__(self, title, id, overview, poster_path, backdrop_path):
        """
        Initializes a new instance of the Movie class.

        Args:
            title (str): The title of the movie.
            id (int): The ID of the movie.
            overview (str): An overview or description of the movie.
            poster_path (str): The relative path to the movie's poster image.
            backdrop_path (str): The relative path to the movie's backdrop image.
        """
        self.name = title
        self.id = id
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w342/' + poster_path
        self.backdrop = 'https://image.tmdb.org/t/p/w1280/' + backdrop_path


class Show:
    """
    Represents a TV show.

    Attributes:
        name (str): The name of the TV show.
        id (int): The ID of the TV show.
        overview (str): An overview or description of the TV show.
        poster (str): The URL of the TV show's poster image.
        backdrop (str): The URL of the TV show's backdrop image.
    """

    def __init__(self, name, id, overview, poster_path, backdrop_path):
        """
        Initializes a new instance of the Show class.

        Args:
            name (str): The name of the TV show.
            id (int): The ID of the TV show.
            overview (str): An overview or description of the TV show.
            poster_path (str): The relative path to the TV show's poster image.
            backdrop_path (str): The relative path to the TV show's backdrop image.
        """
        self.name = name
        self.id = id
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w342/' + poster_path
        self.backdrop = 'https://image.tmdb.org/t/p/w1280/' + backdrop_path
