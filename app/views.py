# import render template function
from flask import render_template

# Import app instance
from app import app

# Generate view functions

@app.route('/')
def index():
    '''
    Index view function loaded to display homepage information
    '''
    message='Hello, World'

    return render_template('index.html',message=message)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    Movie view function to display details of a particular movie
    Args:
        1. movie_id:The unique id of the movie being displayed
    '''

    return render_template('movie.html',id=movie_id)
