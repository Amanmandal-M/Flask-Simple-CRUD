from flask import Blueprint, render_template, request
from controllers.crud_controllers import create, read, update, delete

crud_route = Blueprint('crud', __name__)

crud_route.route('/create', methods=['GET', 'POST'])(create)

crud_route.route('/read')(read)

crud_route.route('/update', methods=['GET', 'POST'])(update)

crud_route.route('/delete', methods=['GET', 'POST'])(delete)
