# imports
import requests

# constants
OPEN_FOOD_FACTS_BASE_URL = 'https://world.openfoodfacts.org'


# search api for product
def search_product_name(product_name):
    '''
    Retrieves product from api
    - Uses search endpoint
    - Field retrieved are fixed
    - Returns first result from response list
    '''

    # construct request properties
    endpoint = '/api/v2/search' # search endpoint
    fields = [
        'id', 'product_name', 'product_type', 'quantity',

    ] # list of fields to return
    fields_concat = ','.join(fields) # concatenate for request parameter

    # construct request parameter
    params = {
        'product_name': product_name,
        'fields': fields_concat,
    }

    # make request
    response = requests.get(url=f"{OPEN_FOOD_FACTS_BASE_URL}{endpoint}", params=params)
    response.raise_for_status()
    
    # parse response
    data = response.json()
    products = data.get('products', [])

    # return product (if exists)
    if not products:
        print(f"No product `{product_name}` found.")
        return {}
    return products[:1]