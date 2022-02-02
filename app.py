from src.server import MyApp

app_instance = MyApp()
app = app_instance.create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
