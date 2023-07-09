from flask import Blueprint, render_template, request, jsonify

datas = []

def create():
    """
    Create a new user.
    """
    data = request.get_json()
    user_data = {
        'id': data['id'],
        'name': data['name'],
        'age': data['age'],
    }
    datas.append(user_data)
    return jsonify(user_data)


def read():
    """
    Retrieve all users.
    """
    return jsonify(datas)


def update(id):
    """
    Update a user by ID.
    """
    data = request.get_json()
    for user in datas:
        if user['id'] == id:
            user['name'] = data.get('name', user['name'])
            user['age'] = data.get('age', user['age'])
            return jsonify(user)
    return jsonify({'error': 'User not found'})


def delete(id):
    """
    Delete a user by ID.
    """
    for user in datas:
        if user['id'] == id:
            datas.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'})
