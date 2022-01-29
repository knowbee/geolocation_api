from flask import send_from_directory
from server import create_app
from flask_swagger_ui import get_swaggerui_blueprint
from resources.routes import initialize_routes

app = create_app(initialize_routes)


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Geolocation-Swagger-UI"})

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
if __name__ == "__main__":
    app.run(debug=True, port=8080)
