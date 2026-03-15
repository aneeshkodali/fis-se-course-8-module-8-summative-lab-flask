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