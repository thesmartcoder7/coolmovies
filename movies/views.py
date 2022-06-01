import requests
from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Trending

def get_trending():
    response = requests.get(url='https://api.themoviedb.org/3/trending/all/week?api_key=b7c72ad37773a8eb3a0254f31fafb0fd')
    response.raise_for_status()
    mixed = response.json()['results']
    results = []
    if mixed:
        for item in mixed:
            if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                new = Trending(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                results.append(new)
    return results


def get_latest():
    response = requests.get(url='https://api.themoviedb.org/3/movie/latest?api_key=b7c72ad37773a8eb3a0254f31fafb0fd')
    response.raise_for_status()
    mixed = response.json()['results']
    results = []
    if mixed:
        for item in mixed:
            if item.get('title') and item.get('id') and item.get('overview') and item.get('poster_path') and item.get('backdrop_path'):
                new = Trending(item.get('title'), item.get('id'), item.get('overview'), item.get('poster_path'), item.get('backdrop_path'))
                results.append(new)
    return results


def get_trailer(id):

    response = requests.get(url='https://api.themoviedb.org/3/movie/{}/videos?api_key=b7c72ad37773a8eb3a0254f31fafb0fd&language=en-US'.format(str(id)))
    response.raise_for_status()
    items = response.json()['results']
    video_key = None
    if items:
        for item in items:
            if item.get('type') == 'Trailer':
                video_key = item.get('key')
                return video_key


# Create your views here.
def home(request):
    return render(request, 'movies/index.html')


def movies(request):
    result = get_trending()
    latest = get_latest()
    random.shuffle(result)
    selected = result[0]
    key = get_trailer(selected.id)
    everything = []
    for i in range(11):
        everything.append(result[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'latest': latest
    }
    return render(request, 'movies/everything.html', context)
