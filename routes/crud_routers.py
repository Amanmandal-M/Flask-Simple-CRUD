from flask import Blueprint, render_template, request
from controllers.crud_controllers import create_entry, get_data, update_entry, delete_entry

crud_route = Blueprint('crud', __name__)

@crud_route.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        create_entry(key, value)
    return render_template('create.html')

@crud_route.route('/read')
def read():
    data = get_data()
    return render_template('read.html', data=data)

@crud_route.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        update_entry(key, value)
    return render_template('update.html')

@crud_route.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form.get('key')
        delete_entry(key)
    return render_template('delete.html')
