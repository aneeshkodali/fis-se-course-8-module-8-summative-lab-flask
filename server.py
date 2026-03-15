# imports
from flask import Flask, jsonify

# initialize flask app
app = Flask(__name__)

# define root route
@app.route('/')
def index():
    return jsonify({'message': 'Hello World'}), 200

if __name__ == '__main__':
    app.run(debug=True)