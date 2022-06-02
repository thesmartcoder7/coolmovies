import requests
import os
from dotenv import load_dotenv, find_dotenv
from .models import Movie, Show


load_dotenv(find_dotenv())
api_key = os.getenv('API_KEY')


def get_items(url, type):
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
                if item.get('name') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                    new = Show(item.get('name'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                    results.append(new)

    return results


def get_trailer(id):
    response = requests.get(url=f'https://api.themoviedb.org/3/movie/{str(id)}/videos?api_key={api_key}&language=en-US')
    response.raise_for_status()
    items = response.json()['results']
    video_key = None
    if items:
        for item in items:
            if item.get('type') == 'Trailer':
                video_key = item.get('key')
                return video_key



def get_trending_movies():
    url = f'https://api.themoviedb.org/3/trending/all/week?api_key={api_key}'
    return get_items(url, 'movies')  


def get_upcoming_movies():
    url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'movies')


def get_popular_shows():
    url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'shows')

def get_shows_onair():
    url = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=1'
    return get_items(url, 'shows')



