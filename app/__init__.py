# app/__init__.py

from flask import Flask
from config import app_config


# initialize the app

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    return app

app = create_app('development')
