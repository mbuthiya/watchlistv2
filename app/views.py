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
