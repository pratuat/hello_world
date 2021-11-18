from flask import Flask
# from src.dashboard.dash_app import build_app as build_dash_app

app = Flask(__name__)

@app.route('/')
def home(*args, **kwargs):
    return "This is flask app ...", 200

# build_dash_app(app, '/dash_app/')

app.run(debug=True, host='127.0.0.1', port=4180)
