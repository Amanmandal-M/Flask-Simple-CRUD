from flask import request
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def hello():
    # Use request.args.get() to access query parameters
    secret_key = request.args.get('key')
    return '<h1 style="color:blue;text-align:center">Welcome in Simple Crud Application Using Flask!</h1>'


def greet(username):
    return f"Hello, {username}!"

def farewell(username):
    return f"Goodbye, {username}!"
