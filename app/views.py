# import render template function
from flask import render_template

# Import app instance
from app import app

# Import functions
from .request import get_movies,get_movie
CATEGORY_LIST=["popular"]
# Generate view functions

@app.route('/')
def index():
    '''
    Index view function loaded to display homepage information
    '''
    title = 'Welcome to Watchlist'

    # Making API call
    popular_movies_list = get_movies(CATEGORY_LIST[0])
    return render_template('index.html',title=title,popular=popular_movies_list)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    Movie view function to display details of a particular movie
    Args:
        1. movie_id:The unique id of the movie being displayed
    '''
    movie_request = get_movie(movie_id)
    title = f'Movie {movie_id}'
    return render_template('movie.html',id=movie_id,title=title,movie=movie_request)
