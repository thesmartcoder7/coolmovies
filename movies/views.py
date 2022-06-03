from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .api import * 
import random



# Create your views here.
def home(request):
    return render(request, 'movies/index.html')


@login_required
def all(request):
    result = get_trending_movies()
    almost = get_upcoming_movies()
    all_popular = get_popular_shows()
    all_top = get_top_rated()

    upcoming = []
    popular = []
    top_rated = []
    everything = []

    random.shuffle(result)
    random.shuffle(almost)
    random.shuffle(all_popular)
    random.shuffle(all_top)

    selected = result[0]
    key = get_trailer(selected.id)
    
    for i in range(13):
        everything.append(result[i])

    for i in range(12):
        popular.append(all_popular[i])
        if almost[i] not in everything:
            upcoming.append(almost[i])
    
    for i in range(12):
        if all_top[i] not in all_popular:
            top_rated.append(all_top[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'upcoming': upcoming,
        'popular': popular,
        'top_rated': top_rated
    }
    return render(request, 'movies/everything.html', context)



def movies(request):
    result = get_trending_movies()
    almost = get_upcoming_movies()
    all_top = get_top_rated_movies()
    all_popular = get_popular_movies()

    upcoming = []
    popular = []
    top_rated = []
    everything = []

    random.shuffle(result)
    random.shuffle(almost)
    random.shuffle(all_top)
    random.shuffle(all_popular)

    selected = result[0]
    key = get_trailer(selected.id)
    
    for i in range(13):
        everything.append(result[i])

    for i in range(12):
        if almost[i] not in everything:
            upcoming.append(almost[i])

    for i in range(12):
        if all_popular[i] not in everything:
            popular.append(almost[i])
    
    for i in range(12):
        if all_top[i] not in everything:
            top_rated.append(all_top[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'upcoming': upcoming,
        'popular': popular,
        'top_rated': top_rated
    }
    return render(request, 'movies/movies.html', context)


def tv(request):
    result = get_trending_movies()
    almost = get_upcoming_movies()
    all_top = get_top_rated_movies()
    all_popular = get_popular_movies

    upcoming = []
    popular = []
    top_rated = []
    everything = []

    random.shuffle(result)
    random.shuffle(almost)
    random.shuffle(all_top)

    selected = result[0]
    key = get_trailer(selected.id)
    
    for i in range(13):
        everything.append(result[i])

    for i in range(12):
        if almost[i] not in everything:
            upcoming.append(almost[i])

    for i in range(12):
        if all_popular[i] not in everything:
            popular.append(almost[i])
    
    for i in range(12):
        if all_top[i] not in everything:
            top_rated.append(all_top[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'upcoming': upcoming,
        'popular': popular,
        'top_rated': top_rated
    }
    return render(request, 'movies/series.html', context)




