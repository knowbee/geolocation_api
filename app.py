from flask import send_from_directory
from server import create_app
from services import GeocodingService

app = create_app(geocoding=GeocodingService())


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
