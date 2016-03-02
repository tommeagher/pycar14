# import modules
import json
import unicodecsv

# We'll use a local version of this file from now on to save on
# bandwidth.
# Open the file 'data/bills.json'
with open('data/bills.json', 'r') as f:
    # Convert it to a dict
    data = json.load(f)
    # Each bill is stored in an array in `data` with the key `objects`
    # Create a variable for easy access to the data we care about
    objects = data['objects']
    # Create a csv file to output
    with open('data/bills.csv', 'wb') as o:
        # Create a csv writer. This will help us format the file
        # correctly.
        writer = unicodecsv.writer(o, encoding='utf-8')
        # Write out the header row
        writer.writerow([
            'title',
            'label',
            'number',
            'current_status'
        ])
        # Iterate through each dict in the array `objects`
        for bill in objects:
            writer.writerow([
                bill['title_without_number'],
                bill['bill_type_label'],
                bill['number'],
                bill['current_status']
            ])

