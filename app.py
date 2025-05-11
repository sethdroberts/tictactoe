from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "Getting started"
    
if __name__ == "__main__":
    if os.environ.get('FLASK_ENVIRON') == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True, port=8080)