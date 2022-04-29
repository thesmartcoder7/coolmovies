from app import app
from flask import render_template
from .request import get_movies, get_series


@app.route("/")
def home():
    popular = get_movies("popular")
    return render_template("index.html", popular = popular)


@app.route("/movies")
def movies():
    get_movies("popular")
    return render_template("movies.html")


@app.route("/movie/<int:id>")
def movie(id):
    return "Single movie route"


@app.route("/series")
def series():
    get_series("popular")
    return render_template("series.html")

@app.route("/single-show/<int:id>")
def single_show(id):
    return "Single show route"


@app.errorhandler(404)
def not_found(error):
    return "not found", 404


