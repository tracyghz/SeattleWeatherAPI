import requests

# Define the base URL of your API
base_url = 'http://localhost:443'  # Update with the correct URL

# Define the API endpoint you want to test
endpoint = '/query'

# Define query parameters (if needed)
params = {
    'limit': 5,
    'weather': 'rain'
}

# Send a GET request to the API
response = requests.get(base_url + endpoint, params=params)

# Check the response status code
if response.status_code == 200:
    # The request was successful
    data = response.json()  # Parse the JSON response
    print('API Response:', data)
else:
    # There was an error
    print('API Error - Status Code:', response.status_code)
    print('Response Content:', response.text)
