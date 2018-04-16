from app import app
from flask import render_template

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    404 view function
    '''

    return render_template('404.html'),404
