from flask import Blueprint, render_template, request
from controllers.crud_controllers import create, read, update, delete

# Create a Blueprint for the CRUD routes
crud_route = Blueprint('crud', __name__)

# Define the routes and associate them with the controllers

# Route: Create
# Method: POST
# Description: Creates a new item
crud_route.route('/create', methods=['POST'])(create)

# Route: Read
# Method: GET
# Description: Reads all items
crud_route.route('/read')(read)

# Route: Update
# Method: PATCH
# Description: Updates an item by ID
crud_route.route('/update/<int:id>', methods=['PATCH'])(update)

# Route: Delete
# Method: DELETE
# Description: Deletes an item by ID
crud_route.route('/delete/<int:id>', methods=['DELETE'])(delete)
