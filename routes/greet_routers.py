from flask import Blueprint
from controllers.greet_controllers import hello, greet, farewell

# Create a Blueprint for the greet routes
greet_route = Blueprint('routes', __name__)

# Define the routes and associate them with the controllers

# Route: Hello
# Method: GET
# Description: Returns a simple greeting
greet_route.route('/')(hello)

# Route: Greet
# Method: GET
# Description: Greets the user with their name
greet_route.route('/greet/<username>')(greet)

# Route: Farewell
# Method: GET
# Description: Bids farewell to the user with their name
greet_route.route('/farewell/<username>')(farewell)
