from flask import Blueprint, render_template, request, jsonify

datas = []

def create():
    data = request.get_json()
    user_data = {
            'id': data['id'],
            'name': data['name'],
            'age': data['age'],
           }
    datas.append(user_data)
    return jsonify(user_data)


def read():
    return jsonify(datas)


def update(id):
    data = request.get_json()
    for user in datas:
        if user['id'] == id:
            user['name'] = data.get('name', user['name'])
            user['age'] = data.get('age', user['age'])
            return jsonify(user)
    return jsonify({'error': 'User not found'})


def delete(id):
    for user in datas:
        if user['id'] == id:
            datas.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'})