from flask import Flask
import os

from routes.greet_routers import greet_route
from routes.crud_routers import crud_route


app = Flask(__name__)

# Register the routes blueprint
app.register_blueprint(greet_route)
app.register_blueprint(crud_route)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
