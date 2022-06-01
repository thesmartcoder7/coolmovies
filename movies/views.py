from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'movies/index.html')


def another(request):
    return HttpResponse('this is another page')