from flasgger import Swagger


def configure_swagger(app):
    app.config["SWAGGER"] = {
        "swagger_version": "2.0",
        "title": "Application",
        "specs": [
            {
                "version": "0.0.1",
                "title": "Geolocation API",
                "endpoint": "spec",
                "description": "Retrieve street name based on longitude and latitude or vice versa",
                "termsOfService": "",
                "route": "/application/spec",
            }
        ],
        "static_url_path": "/apidocs",
    }
    Swagger(app)
