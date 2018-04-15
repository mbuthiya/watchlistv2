from flask import Flask

# Init app
app = Flask(__name__,instance_relative_config=True)

# setting up configuration
from .config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)
app.config.from_pyfile("config.py")


#import files
from app import views
