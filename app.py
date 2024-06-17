import os
import flask_cors as cors
from flask import Flask

app = Flask(__name__)
cors.CORS(app)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/api")
def api():
    """Example API route."""
    return {"message": "Hello World!"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))