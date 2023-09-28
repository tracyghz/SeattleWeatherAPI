import logging
import requests

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# create console handler and set level to info
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# add console handler to logger
logger.addHandler(console_handler)

# API base url and endpoints
BASE_URL = 'http://localhost:443'
GET_ENDPOINT = '/get-all'
QUERY_ENDPOINT = '/query'

# Define query parameters
limit_weather_query_params = {
    'limit': 5,
    'weather': 'rain'
}
limit_date_query_params = {
    'limit': 10,
    'date': '2012-01-08'
}

query_params = [limit_weather_query_params, limit_date_query_params]


def test_get_all():
    api = BASE_URL + GET_ENDPOINT
    logger.info(f'Testing API: {api}')
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        logger.info(f'API Response: {data}\n test_get_all is successful!')
    else:
        logger.error(f'API Error - Status Code: {response.status_code}')
        logger.error(f'Response Content: {response.text}')


def test_query():
    api_base = BASE_URL + QUERY_ENDPOINT
    logger.info(f'Testing API: {api_base}')
    for params in query_params:
        response = requests.get(api_base, params=params)
        if response.status_code == 200:
            data = response.json()
            logger.info(f'API Response: {data}\n test_query is successful!')
        else:
            logger.error(f'API Error - Status Code: {response.status_code}')
            logger.error(f'Response Content: {response.text}')

if __name__ == '__main__':
    test_query()
    test_get_all()