# app/__init__.py

from flask import Flask
from config import app_config

# initialize the app

def create_app(config_name):
    
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Register blueprints
    from app.v1.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/maintenance_tracker/api/v1/auth')

    from app.v1.requests import req as req_blueprint
    app.register_blueprint(req_blueprint, url_prefix='/maintenance_tracker/api/v1/requests')



    return app

# app = create_app('development')
