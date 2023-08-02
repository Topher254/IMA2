import os
from flask import Flask, send_from_directory, request
from flask_cors import CORS


app = Flask(__name__, static_folder='webapp/dist')

CORS(app)
# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route("/test")
def test():
    return {"test":"Hello World"}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000),host="0.0.0.0")