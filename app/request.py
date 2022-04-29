from app import app
from app import keys
import urllib.request, json
from .models import movie, show

Movie = movie.Movie
Show = show.Show


def get_movies(category):
    request_url = keys.movies_endpoint.format(category, keys.api_token)
    with urllib.request.urlopen(request_url) as url:
        data = url.read()
        response = json.loads(data)
    
    movies_list = get_list(response)
        
    return movies_list

def get_series(category):
    request_url = keys.series_endpoint.format(category, keys.api_token)
    with urllib.request.urlopen(request_url) as url:
        data = url.read()
        response = json.loads(data)

    series = get_list(response)

    return series


def get_list(response):
        new_list = []
        if response["results"]:
            for item in response["results"]:
                if item["poster_path"]:
                    if "original_title" in item.keys():
                        new_list.append(Movie(item["id"], item["original_title"], item["overview"], item["poster_path"]))
                    else:
                        new_list.append(Show(item["id"], item["name"], item["overview"], item["poster_path"]))

        return new_list