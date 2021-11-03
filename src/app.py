from flask import Flask


app = Flask(__name__)

@app.route('/')
def home(*args, **kwargs):
    return 'hello world', 200

app.run()