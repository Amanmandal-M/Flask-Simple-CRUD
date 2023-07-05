data = {}

def create_entry(key, value):
    data[key] = value

def get_data():
    return data

def update_entry(key, value):
    if key in data:
        data[key] = value

def delete_entry(key):
    if key in data:
        del data[key]
