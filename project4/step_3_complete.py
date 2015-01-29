#!/usr/bin/env python

import json

import unicodecsv

def main():
    # We'll use a local version of this file from now on to save on
    # bandwidth.
    with open('bills.json', 'r') as f:
        data = json.load(f)
        objects = data['objects']

        # Create a csv file to output
        with open('bills.csv', 'w') as o:
            # Create a csv writer. This will help us format the file
            # correctly.
            writer = unicodecsv.writer(o, encoding='utf-8')

            # Write out the header row
            writer.writerow([
                u'title',
                u'label',
                u'number',
                u'current_status'
            ])

            # Iterate through each dict in the array `objects`
            for bill in objects:
                writer.writerow([
                    bill['title_without_number'],
                    bill['bill_type_label'],
                    bill['number'],
                    bill['current_status']
                ])

if __name__ == '__main__':
    main()

