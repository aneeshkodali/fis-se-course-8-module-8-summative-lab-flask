# Flask Inventory Management System

## About

This project comprises of an inventory management system that will allow employees to add, edit, view, and delete inventory items. Additionally, the system will fetch real-time product data from an external API (e.g., OpenFoodFacts API) to supplement product details. Overall the system includes (but is not limited to):
- A Flask-based REST API with CRUD operations for managing inventory.
- An external API integration to fetch product details by barcode or name.
- A CLI-based interface to interact with the API.
- Unit tests to validate functionality and interactions.

## File Structure

The following file/folder structure is:
- [`server.py`](./server.py): contains backend routes and view functions for performing CRUD operations on items data
- [`utils`](./utils/): contains helper functions

## Project Use

To use this repository:

### Installation

Clone the repository:
```sh
git clone https://github.com/aneeshkodali/fis-se-course-8-module-8-summative-lab-flask.git
```

Make sure you are in the root repository:
```sh
cd fis-se-course-8-module-8-summative-lab-flask
```

Install necessary libraries (for virtual environment):
```sh
pipenv install
```

Activate virtual environment:
```sh
pipenv shell
```

### Server

Run the server:
```sh
python server.py
```

### API Endpoints

#### GET /inventory
Returns all inventory items

#### GET /inventory/<id>
Returns a single inventory item by ID

#### POST /inventory
Creates a new inventory item

Request body:
```json
{
  "product": "almond milk",
  "quantity": 10,
  "price": 5
}
```

#### PATCH /inventory/<id>
Updates an inventory item

Request body:
```json
{
  "price": 8
}
```

#### DELETE /inventory/<id>
Deletes an inventory item

### CLI

To use the CLI (make sure server is running in a separate terminal):

```sh
python cli.py <command> [options]
```

### CLI Commands

#### List inventory items
```sh
python cli.py list-inventory
```

#### Get a single inventory item
```sh
python cli.py get-inventory --id 1
```

#### Add a new inventory item
```sh
python cli.py add-inventory --product "almond milk" --quantity 10 --price 5
```

#### Update an inventory item
```sh
python cli.py update-inventory --id 1 --price 7
```

```sh
python cli.py update-inventory --id 1 --quantity 15
```

```sh
python cli.py update-inventory --id 1 --price 7 --quantity 15
```

#### Delete an inventory item
```sh
python cli.py delete-inventory --id 1
```

### Testing

Run tests using:

```sh
pytest -x
```