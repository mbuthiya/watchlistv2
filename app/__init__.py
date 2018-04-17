from flask import Flask

# Init app
app = Flask(__name__,instance_relative_config=True)

#import 3rd party apps
from flask_bootstrap import Bootstrap

# setting up configuration
from .config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)
app.config.from_pyfile("config.py") # Instance config

#Initializing flask extensions
bootstrap = Bootstrap(app)

#import files
from app import views,error
