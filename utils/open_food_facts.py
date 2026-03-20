# imports
import requests

# constants
OPEN_FOOD_FACTS_BASE_URL = 'https://world.openfoodfacts.org'
OPEN_FOOD_FACTS_FIELD_LIST = [
    'code', 'product_name', 'brands', 'quantity', 'image_url', 'nutriscore_grade',
] # assumes these fields that are to be returned are FIXED

# create variables from constants
OPEN_FOOD_FACTS_FIELD_LIST_CONCAT = ','.join(OPEN_FOOD_FACTS_FIELD_LIST)


# search api for product based on name
def search_product(search_term):
    '''
    Retrieves product from api
    - Uses search endpoint
    - Returns first result from response list
    '''

    # construct request parameter
    endpoint = '/cgi/search.pl'
    api_url = f"{OPEN_FOOD_FACTS_BASE_URL}{endpoint}"
    params = {
        'search_terms': search_term,
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
        print(f"No product with  `{search_term}` found.")
        return {}
    return product