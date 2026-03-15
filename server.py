# imports
from flask import Flask, jsonify
from utils.storage import load_data

# initialize flask app
app = Flask(__name__)

# read inventory data
inventory_data = load_data(file_path='data/inventory.json')

# '/' route
# returns a welcome message
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Inventory Management System!'}), 200

# '/inventory' route
# returns full list of inventory in JSON
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory_data), 200

# '/inventory/<id>' route
# retrieves inventory data for given id
@app.route('/inventory/<int:id>')
def get_inventory_by_id(id):

    # get inventory item from list
    inventory_item = next(
        (i for i in inventory_data if i.id == id),
        None
    )

    # return item data
    if inventory_item:
        return jsonify(inventory_item), 200
    return jsonify({"error": f"Inventory item with ID {id} not found"}), 404 # return error if not found


if __name__ == '__main__':
    app.run(debug=True)