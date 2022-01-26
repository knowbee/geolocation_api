from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from resources.routes import initialize_routes
from database.db import db

import os

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db.init_app(app)
Migrate(app, db)

api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
