import urllib.request
import json
from urllib.error import URLError # Import the error class

from app import app
from .models.movie import Movie

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
    
    # Request with error handling
    try:
        with urllib.request.urlopen(get_movies_url) as movies:
            movie_response = movies.read()
            movie_dictionary = json.loads(movie_response)

        if movie_dictionary['results']:
            unedited_movie_list = movie_dictionary['results']
            final_movie_list = process_movie_results(unedited_movie_list)
        else:
            final_movie_list = []

    except URLError:
        print("woops")

    return final_movie_list



def process_movie_results(unedited_movie_list):
    '''
    Takes in a dictionary of movies and loops through them creating instances of the Movie class with the properities needed.

    Args:
        unedited_movie_list a list of movie dictionaries
    '''

    processed_movie_list =[]

    for movie_dict in unedited_movie_list:
        if approved_movie(movie_dict):
            id = movie_dict.get("id")
            title=movie_dict.get("original_title")
            overview=movie_dict.get("overview")
            image =movie_dict.get("poster_path")
            vote_average =movie_dict.get("vote_average")
            vote_count =movie_dict.get("vote_count")

            # Generate movie object
            movie_dict_object = Movie(id,title,overview,image,vote_average,vote_count)

    return processed_movie_list

def approved_movie(movie_dict):
    '''
    Checks to see if all the properities are available to create a new movie object

    Args:
        movie_dict : A movie dictionary
    '''

    if movie_dict["id"] and movie_dict["original_title"] and movie_dict["overview"] and movie_dict["poster_path"] and movie_dict["vote_average"] and movie_dict["vote_count"]:
        return True
    else:
        return False
