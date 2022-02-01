from src.server import create_app
from src.helpers import GeocodingWrapper

app = create_app(geocoding=GeocodingWrapper())
if __name__ == "__main__":
    app.run(debug=True, port=8080)
