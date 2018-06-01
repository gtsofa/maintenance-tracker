# app/v1/requests/__init__.py

from flask import Blueprint

#blueprint object
req = Blueprint('req', __name__)

from . import views