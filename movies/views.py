from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .api import * 
import random



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
    for i in range(13):
        everything.append(result[i])

    for i in range(12):
        upcoming.append(almost[i])
    
    context = {
        'trending': selected,
        'trailer': key,
        'everything': everything,
        'upcoming': upcoming
    }
    return render(request, 'movies/everything.html', context)
