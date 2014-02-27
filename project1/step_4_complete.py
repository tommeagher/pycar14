# import modules
import csv

# write a function to output the first row of a csv file
# and get the column names
def output_first_csv_row(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # create a variable to represent the header row
    header_row = csv_data.next()

    # output the value
    print header_row

    # output the length of the header row
    print len(header_row)

    # output the type of the header row
    print type(header_row)

    # loop through each item in the header_row
    for column_name in header_row:

        # output its contents
        print column_name

        # output its length
        print len(column_name)

        # output its type
        print type(column_name)

    # close the csv file when we're done
    csv_file.close()

output_first_csv_row('fdic_failed_bank_list.csv')