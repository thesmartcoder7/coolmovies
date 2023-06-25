import requests
import os
from dotenv import load_dotenv, find_dotenv
from .models import Movie, Show

load_dotenv(find_dotenv())
api_key = os.getenv('API_KEY')

def get_items(url, type):
    """
    Retrieves items from a given API endpoint URL based on the specified type.

    Args:
        url (str): The URL of the API endpoint.
        type (str): The type of items to retrieve. Valid values are 'movies' and 'shows'.

    Returns:
        list: A list of Movie or Show objects.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    response = requests.get(url)
    response.raise_for_status()
    mixed = response.json()['results']
    results = []

    if mixed:
        if type == 'movies':
            for item in mixed:
                if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                    new = Movie(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                    results.append(new)
        else:
            for item in mixed:
                # and item.get('overview')
                if item.get('original_name') and item.get('id')  and item.get('poster_path') and item.get('backdrop_path'):
                    new = Show(item.get('name'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                    results.append(new)

    return results

def check_trailer(id, type):
    """
    Checks if a movie or show with the specified ID has a trailer.

    Args:
        id (int): The ID of the movie or show.
        type (str): The type of item. Valid values are 'movies' and 'shows'.

    Returns:
        bool: True if a trailer is found, False otherwise.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    if type == 'movies':
        response = requests.get(url=f'https://api.themoviedb.org/3/movie/{str(id)}/videos?api_key={api_key}&language=en-US')
    else:
        response = requests.get(url=f'https://api.themoviedb.org/3/tv/{str(id)}/videos?api_key={api_key}&language=en-US')
    response.raise_for_status()
    items = response.json()['results']
    if items:
        for item in items:
            if item.get('type') and item.get('type') == 'Trailer':
               return True

def get_trailer(id, type):
    """
    Retrieves the trailer key for a movie or show with the specified ID.

    Args:
        id (int): The ID of the movie or show.
        type (str): The type of item. Valid values are 'movies' and 'shows'.

    Returns:
        str: The trailer key if found, None otherwise.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    if type == 'movies':
        response = requests.get(url=f'https://api.themoviedb.org/3/movie/{str(id)}/videos?api_key={api_key}&language=en-US')
    else:
        response = requests.get(url=f'https://api.themoviedb.org/3/tv/{str(id)}/videos?api_key={api_key}&language=en-US')
    response.raise_for_status()
    items = response.json()['results']
    video_key = None
    if items:
        for item in items:
            if item.get('type') == 'Trailer':
                video_key = item.get('key')
                return video_key

# movie requests

def get_trending_movies():
    """
    Retrieves the trending movies of the week.

    Returns:
        list: A list of Movie objects representing the trending movies.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/trending/all/week?api_key={api_key}'
    return get_items(url, 'movies')

def get_upcoming_movies():
    """
    Retrieves the upcoming movies.

    Returns:
        list: A list of Movie objects representing the upcoming movies.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')

def get_top_rated_movies():
    """
    Retrieves the top-rated movies.

    Returns:
        list: A list of Movie objects representing the top-rated movies.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')

def get_popular_movies():
    """
    Retrieves the popular movies.

    Returns:
        list: A list of Movie objects representing the popular movies.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')

# tv requests

def get_popular_shows():
    """
    Retrieves the popular TV shows.

    Returns:
        list: A list of Show objects representing the popular TV shows.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'shows')

def get_top_rated_shows():
    """
    Retrieves the top-rated TV shows.

    Returns:
        list: A list of Show objects representing the top-rated TV shows.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'shows')

def get_trending_shows():
    """
    Retrieves the trending TV shows.

    Returns:
        list: A list of Show objects representing the trending TV shows.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')

def get_upcoming_shows():
    """
    Retrieves the upcoming TV shows.

    Returns:
        list: A list of Show objects representing the upcoming TV shows.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error response.
    """
    url = f'https://api.themoviedb.org/3/tv/airing_today?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')
