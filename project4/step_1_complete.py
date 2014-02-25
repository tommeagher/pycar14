# `json` is a module that helps us use the JSON data format.
import json

# `requests` is a module for interacting with the Internet
import requests

def main():
    url = 'https://www.govtrack.us/api/v2/bill?congress=112&order_by=-current_status_date'

    # Read the `requests` documentation for information. I promise it
    # isn't that scary.
    # http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

    # Request the data
    r = requests.get(url)

    # Since we know our data will be JSON, let's automatically convert
    # it to a Python dict.
    data = r.json()

    # -- OR -- If the network is down, we can use a local version of this file.
    #with open('bills.json', 'r') as f:
    #    data = json.load(f)

    # `json.dumps()` is a way to print a Python dict in a more
    # human-readable way.
    print json.dumps(data, indent=4)

if __name__ == '__main__':
    main()

