from src.server import create_app
from src.helpers import Geocoding

app = create_app(geocoding=Geocoding())
if __name__ == "__main__":
    app.run(debug=True, port=8080)
