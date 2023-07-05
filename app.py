from flask import Flask

from routes.greet_routers import greet_route
from routes.crud_routers import crud_route


app = Flask(__name__)

# Register the routes blueprint
app.register_blueprint(greet_route)
app.register_blueprint(crud_route)


if __name__ == '__main__':
    app.run()
