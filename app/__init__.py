from flask import Flask

# Init app
app = Flask(__name__)

# setting up configuration
from .config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

#import files
from app import views
