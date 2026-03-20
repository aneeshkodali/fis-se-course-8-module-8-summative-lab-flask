# imports
import argparse
import requests

# constants
BASE_URL = 'http://127.0.0.1:5000'

# get inventory
def get_inventory(**kwargs):

    # make request
    response = requests.get(url=f"{BASE_URL}/inventory")
    if response.status_code != 200:
        print("Error:", response.json())
        return
    print(response.json())

# get inventory item
def get_inventory_item(id, **kwargs):

    # make request
    response = requests.get(url=f"{BASE_URL}/inventory/{id}")
    if response.status_code != 200:
        print("Error:", response.json())
        return
    print(response.json())

# add inventory item
def add_inventory_item(product, quantity, price, **kwargs):

    # construct request payload
    payload = {
        'product': product,
        'quantity': quantity,
        'price': price,
    }

    # make request
    response = requests.post(url=f"{BASE_URL}/inventory", json=payload)
    if response.status_code != 201:
        print("Error:", response.json())
        return
    print(response.json())

# update inventory item
def update_inventory_item(id, quantity=None, price=None, **kwargs):

    if (quantity is None) and (price is None):
        print("No update payload found")
        return

    # construct request payload
    payload = {}
    if quantity is not None:
        payload['quantity'] = quantity
    if price is not None:
        payload['price'] = price

    # make request
    response = requests.patch(url=f"{BASE_URL}/inventory/{id}", json=payload)
    if response.status_code != 200:
        print("Error:", response.json())
        return
    print(response.json())

# delete inventory item
def delete_inventory_item(id, **kwargs):

    # make request
    response = requests.delete(url=f"{BASE_URL}/inventory/{id}")
    if response.status_code != 200:
        print("Error:", response.json())
        return
    print(response.json())


def main():

    # initialize parser
    parser = argparse.ArgumentParser(description="Inventory Management System CLI")

    # initialize subparsers
    subparsers = parser.add_subparsers(dest='command')

    # list-inventory
    list_inventory_parser = subparsers.add_parser('list-inventory')
    list_inventory_parser.set_defaults(func=get_inventory)

    # get-inventory
    get_inventory_parser = subparsers.add_parser('get-inventory')
    get_inventory_parser.add_argument('--id', type=int, required=True, help='Product ID')
    get_inventory_parser.set_defaults(func=get_inventory_item)

    # add-inventory
    add_inventory_parser = subparsers.add_parser('add-inventory')
    add_inventory_parser.add_argument('--product', type=str, required=True, help='Product to search/add')
    add_inventory_parser.add_argument('--price', type=float, required=True, help='Product price')
    add_inventory_parser.add_argument('--quantity', type=int, required=True, help='Product quantity in stock')
    add_inventory_parser.set_defaults(func=add_inventory_item)

    # update-inventory
    update_inventory_parser = subparsers.add_parser('update-inventory')
    update_inventory_parser.add_argument('--id', type=int, required=True, help='Product ID')
    update_inventory_parser.add_argument('--price', type=float, help='Product price')
    update_inventory_parser.add_argument('--quantity', type=int, help='Product quantity in stock')
    update_inventory_parser.set_defaults(func=update_inventory_item)

    # delete-inventory
    delete_inventory_parser = subparsers.add_parser('delete-inventory')
    delete_inventory_parser.add_argument('--id', type=int, required=True, help='Product ID')
    delete_inventory_parser.set_defaults(func=delete_inventory_item)

    # parse args from command line
    args = parser.parse_args()
    # check if func/subcommand passed
    if hasattr(args, 'func'):
        args.func(**vars(args))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()