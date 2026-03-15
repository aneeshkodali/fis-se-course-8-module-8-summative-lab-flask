# imports
import requests

# constants
OPEN_FOOD_FACTS_BASE_URL = 'https://world.openfoodfacts.org'
OPEN_FOOD_FACTS_FIELD_LIST = [
    'id', 'product_name', 'product_type', 'quantity',
] # assumes these fields that are to be returned are FIXED

# create variables from constants
OPEN_FOOD_FACTS_FIELD_LIST_CONCAT = ','.join(OPEN_FOOD_FACTS_FIELD_LIST)


# search api for product based on name
def search_product_name(product_name):
    '''
    Retrieves product from api
    - Uses search endpoint
    - Returns first result from response list
    '''

    # construct request parameter
    endpoint = '/cgi/search.pl'
    api_url = f"{OPEN_FOOD_FACTS_BASE_URL}{endpoint}"
    params = {
        'search_terms': product_name,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        'fields': OPEN_FOOD_FACTS_FIELD_LIST_CONCAT,
    }

    # make request
    response = requests.get(url=api_url, params=params)
    response.raise_for_status()
    data = response.json()
    products = data.get('products', [])

    # return product (if exists)
    product = products[0] if products else None
    if not product:
        print(f"No product with name `{product_name}` found.")
        return {}
    return product

# search api for product based on id
def search_product_id(product_id):
    '''
    Retrieves product from api
    - Uses search endpoint
    - Returns first result from response list
    - Assumes that barcode and id are identical
    '''

    # construct request parameter
    endpoint = f"/api/v2/product/{product_id}.json"
    api_url = f"{OPEN_FOOD_FACTS_BASE_URL}{endpoint}"
    params = {
        'fields': OPEN_FOOD_FACTS_FIELD_LIST_CONCAT,
    }

    # make request
    response = requests.get(url=api_url, params=params)

    if response.status_code == 404:
        print(f"No product with ID {product_id} found.")
        return {}
    
    response.raise_for_status()

    # parse product from response
    data = response.json()
    product = data.get('product', {})
    
    return product