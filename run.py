from app import app

app.config.from_pyfile('config.py')

if __name__ == "__main__":
    app.run(debug = True)