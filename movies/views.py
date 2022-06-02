import requests
import os
from dotenv import load_dotenv, find_dotenv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random
from .models import Movie



load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')


def get_trending():
    response = requests.get(url=f'https://api.themoviedb.org/3/trending/all/week?api_key={api_key}')
    response.raise_for_status()
    mixed = response.json()['results']
    results = []
    if mixed:
        for item in mixed:
            if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                new = Movie(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                results.append(new)
    return results


def get_upcoming():
    response = requests.get(url=f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1')
    response.raise_for_status()
    mixed = response.json()['results']
    results = []
    if mixed:
        for item in mixed:
            if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                new = Movie(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
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


def get_top_shows():
    response = requests.get(url=f'https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=en-US&page=1')
    response.raise_for_status()
    mixed = response.json()['results']
    results = []
    if mixed:
        for item in mixed:
            if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                new = Movie(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                results.append(new)
    return results


# Create your views here.
def home(request):
    return render(request, 'movies/index.html')


@login_required
def movies(request):
    result = get_trending()
    almost = get_upcoming()
    upcoming = []
    
    random.shuffle(result)
    selected = result[0]
    key = get_trailer(selected.id)
    everything = []
    for i in range(11):
        everything.append(result[i])

    for i in range(10):
        upcoming.append(almost[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'upcoming': upcoming
    }
    return render(request, 'movies/everything.html', context)
