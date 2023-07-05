from flask import request
from dotenv import load_dotenv
import os

load_dotenv()


def hello():
    # Use request.args.get() to access query parameters
    secret_key = request.args.get('key')
    return 'Welcome in Flask Project'


def greet(username):
    return f"Hello, {username}!"


def farewell(username):
    return f"Goodbye, {username}!"
