# app/__init__.py

from flask import Flask, request, jsonify, abort

# initialize the app
app = Flask(__name__)