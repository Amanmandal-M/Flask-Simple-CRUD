from flask import Blueprint, render_template, request

data = {}

def create():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        data[key] = value
    return data

def read():
    return data


def update():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key in data:
            data[key] = value
    return render_template('update.html')

        
def delete():
    if request.method == 'POST':
        key = request.form.get('key')
        if key in data:
            del data[key]
    return render_template('delete.html')        
