from flask import Blueprint
from controllers.greet_controllers import hello, greet, farewell

greet_route = Blueprint('routes', __name__)

# Define the routes and associate them with the controllers
greet_route.route('/')(hello)
greet_route.route('/greet/<username>')(greet)
greet_route.route('/farewell/<username>')(farewell)
