import urllib.request
import json

from app import app
from models.movie import Movie

API_KEY = app.config['MOVIE_API_KEY']
BASE_URL = app.config['MOVIE_BASE_URL']



def get_movies(category):
    '''
    Request function that takes a movie category and returns a list of movies

    Args:
        category: category of movies to search for.
    '''

    # Formating the base url with our category and key
    get_movies_url = BASE_URL.format(category,API_KEY)

    # Create empty movie dictionary
    movie_dictionary ={}
    final_movie_list =[]
    # Request
    with urllib.request.urlopen(get_movies_url) as movies:
        movie_response = movies.read()
        movie_dictionary = json.loads(movie_response)

    if movie_dictionary['results']:
        unedited_movie_list = movie_dictionary['results']
        final_movie_list = process_movie_results(unedited_movie_list)
    else:
        final_movie_list = []

    return final_movie_list
