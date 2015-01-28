import json

import requests

def main():
    # We'll use a local version of this file from now on to save on
    # bandwidth.
    with open('bills.json', 'r') as f:
        data = json.load(f)

        # Each bill is stored in an array in `data` with the key `objects`
        objects = data['objects']

        # Iterate through each dict in the array `objects`
        for bill in objects:
            print json.dumps(bill, indent=4)

if __name__ == '__main__':
    main()

