# imports
from flask import Flask, jsonify, request
from utils.open_food_facts import search_product
from utils.storage import load_data, save_data

# initialize flask app
app = Flask(__name__)

# constants
INVENTORY_FILE = 'data/inventory.json'

# '/' route
# returns a welcome message
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Inventory Management System!'}), 200

# '/inventory' route
# returns full list of inventory in JSON
@app.route('/inventory', methods=['GET'])
def get_inventory():

    # read in data
    inventory_data = load_data(file_path=INVENTORY_FILE)

    return jsonify(inventory_data), 200

# '/inventory/<id>' route
# retrieves inventory data for given item id
@app.route('/inventory/<int:id>', methods=['GET'])
def get_inventory_by_id(id):

    # read in data
    inventory_data = load_data(file_path=INVENTORY_FILE)

    # get inventory item from list
    inventory_item = next(
        (i for i in inventory_data if i['id'] == id),
        None
    )

    # exit if no item found
    if not inventory_item:
        return jsonify({"error": f"Inventory item with ID {id} not found"}), 404 # return error if not found
    
    return jsonify(inventory_item), 200

# create new inventory item
@app.route('/inventory', methods=['POST'])
def create_inventory():

    # get incoming request data
    data = request.get_json()

    # exit if not product in request data
    if (not data) or (not data.get('product')):
        return jsonify({'message': 'Product not found in request'}), 400
    
    # read in inventory data
    inventory_data = load_data(file_path=INVENTORY_FILE)

    # get next available id
    new_id = max((i['id'] for i in inventory_data), default=0) + 1
    
    # create new inventory item
    product_api_data = search_product(search_term=data.get('product')) or {}
    new_inventory = {
        **{'id': new_id},
        **data,
        **product_api_data,
    }

    # append to existing data
    inventory_data.append(new_inventory)

    # save and return inventory
    save_data(file_path=INVENTORY_FILE, data=inventory_data)
    return jsonify(new_inventory), 201

# update inventory item
@app.route('/inventory/<int:id>', methods=['PATCH'])
def update_inventory(id):

    # get incoming request data
    data = request.get_json()

    # exit if no request data
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # remove id (if exists) from request data
    data.pop('id', None)

    # read in inventory data
    inventory_data = load_data(file_path=INVENTORY_FILE)

    # set variable to keep track of update
    update_bool = False

    # loop through inventory data
    for i, inventory_item in enumerate(inventory_data):

        # look for item based on id
        if inventory_item['id'] == id:

            # update item
            inventory_data[i] = {
                **inventory_item,
                **data, # make sure data is 2nd so it's data overwrites prior data
            }
            updated_item = inventory_data[i]
            # update bool
            update_bool = True

            # break out of loop
            break

    if not update_bool:
        # exit if no item found
        return jsonify({"error": f"Inventory item with ID {id} not found"}), 404 # return error if not found
    
    # save data
    save_data(file_path=INVENTORY_FILE, data=inventory_data)
    return jsonify(updated_item), 200

# delete inventory
@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory(id):

    # read in inventory data
    inventory_data = load_data(file_path=INVENTORY_FILE)

    # set variable to keep track of delete
    delete_bool = False

    # loop through inventory data
    for i, inventory_item in enumerate(inventory_data):

        # look for item based on id
        if inventory_item['id'] == id:

            # delete item
            del inventory_data[i]

            # update bool
            delete_bool = True

            # break out of loop
            break

    if not delete_bool:
        # exit if no item found
        return jsonify({"error": f"Inventory item with ID {id} not found"}), 404 # return error if not found
    
    # save data
    save_data(file_path=INVENTORY_FILE, data=inventory_data)
    return jsonify({'message': f"Inventory item with ID {id} deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)