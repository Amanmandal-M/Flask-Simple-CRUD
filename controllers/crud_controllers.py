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
            user['name'] = data['name'] 
            user['age'] = data['age'] 
            return jsonify(user)
    return jsonify({'error': 'User not found'})

        
def delete(id):
    for user in users:
        if user['id'] == id:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'user not found'})      
