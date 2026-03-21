# force Python to include project root in path
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# set env var (before importing server)
os.environ['INVENTORY_FILE'] = 'data/test_inventory_cli.json'

# imports
from server import app
from utils.storage import save_data
import cli
import requests

# constants
BASE_URL = 'http://127.0.0.1:5000'
TEST_FILE = os.environ['INVENTORY_FILE']

def reset_file():
    """
    Reset test inventory file before each test.
    """
    save_data(TEST_FILE, [])


def test_cli_add():
    """
    Add item via CLI, then verify via API.
    """
    reset_file()

    cli.add_inventory_item("milk", 10, 5)

    response = requests.get(f"{cli.BASE_URL}/inventory")
    data = response.json()

    assert len(data) >= 1


def test_cli_update():
    """
    Update item via CLI, then verify via API.
    """
    reset_file()

    # create item via API
    response = requests.post(f"{cli.BASE_URL}/inventory", json={
        "product": "milk",
        "quantity": 10,
        "price": 5
    })
    item = response.json()

    # update via CLI
    cli.update_inventory_item(item['id'], price=8)

    # verify
    response = requests.get(f"{cli.BASE_URL}/inventory/{item['id']}")
    data = response.json()

    assert data["price"] == 8


def test_cli_delete():
    """
    Delete item via CLI, then verify it's gone.
    """
    reset_file()

    # create item via API
    response = requests.post(f"{cli.BASE_URL}/inventory", json={
        "product": "milk",
        "quantity": 10,
        "price": 5
    })
    item = response.json()

    # delete via CLI
    cli.delete_inventory_item(item['id'])

    # verify deletion
    response = requests.get(f"{cli.BASE_URL}/inventory/{item['id']}")
    assert response.status_code == 404