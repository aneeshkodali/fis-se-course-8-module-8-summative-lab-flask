# force Python to include project root in path
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# set env var (before importing server)
os.environ['INVENTORY_FILE'] = 'data/test_inventory_server.json'

# imports
from server import app
from utils.storage import save_data



# constants
TEST_FILE = os.environ['INVENTORY_FILE']


def reset_file():
    """
    Reset the test inventory file before each test.
    """
    save_data(TEST_FILE, [])


def test_get_inventory():
    """
    Test retrieving all inventory items.
    Expect an empty list when no data exists.
    """
    reset_file()

    client = app.test_client()
    response = client.get('/inventory')

    assert response.status_code == 200
    assert response.get_json() == []


def test_create_inventory():
    """
    Test creating a new inventory item.
    Expect a 201 response (created).
    """
    reset_file()

    client = app.test_client()

    response = client.post('/inventory', json={
        "product": "milk",
        "quantity": 10,
        "price": 5
    })

    assert response.status_code == 201


def test_update_inventory():
    """
    Test updating an existing inventory item.
    Expect a 200 response after update.
    """
    reset_file()

    client = app.test_client()

    # create an item first
    response = client.post('/inventory', json={
        "product": "milk",
        "quantity": 10,
        "price": 5
    })
    item = response.get_json()

    # update the item
    response = client.patch(f"/inventory/{item['id']}", json={
        "price": 8
    })

    assert response.status_code == 200


def test_delete_inventory():
    """
    Test deleting an inventory item.
    Expect a 200 response after deletion.
    """
    reset_file()

    client = app.test_client()

    # create an item first
    response = client.post('/inventory', json={
        "product": "milk",
        "quantity": 10,
        "price": 5
    })
    item = response.get_json()

    # delete the item
    response = client.delete(f"/inventory/{item['id']}")

    assert response.status_code == 200