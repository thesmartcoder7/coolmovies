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
    all_top = get_top_rated_shows()

    upcoming = []
    popular = []
    top_rated = []
    everything = []

    random.shuffle(result)
    random.shuffle(almost)
    random.shuffle(all_popular)
    random.shuffle(all_top)

    selected = result[0]
    key = get_trailer(selected.id, 'movies')

    if len(result) > 13:
        for i in range(13):
            try:
                everything.append(result[i])
            except:
                pass
    else:
        for i in range(7):
            try:
                everything.append(result[i])
            except:
                pass

    if len(all_popular) > 12:
        for i in range(12):
            try:
                popular.append(all_popular[i])
                if almost[i] not in everything:
                    upcoming.append(almost[i])
            except:
                pass
    else:
        for i in range(6):
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


@login_required
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
    key = get_trailer(selected.id, 'movies')

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


@login_required
def tv(request):
    result = get_popular_shows()
    almost = get_top_rated_shows()
    all_popular = get_popular_shows()
    all_top = get_top_rated_shows()

    upcoming = []
    popular = []
    top_rated = []
    everything = []

    random.shuffle(result)
    random.shuffle(almost)
    random.shuffle(all_popular)
    random.shuffle(all_top)

    selected = None
    for item in result:
        if check_trailer(item.id, 'tv'):
            selected = item
    key = get_trailer(selected.id, 'tv')

    for i in range(12):
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
    return render(request, 'movies/series.html', context)
