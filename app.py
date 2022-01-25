from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_envvar("APP_CONFIG_FILE")

from resources.routes import initialize_routes

api = Api(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(port=5000, debug=False)
