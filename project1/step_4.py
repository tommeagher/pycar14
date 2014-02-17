# import modules
import csv

# write your function passing in the file name
def open_csv_file(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # create a variable to represent the header row
    header_row = csv_data.next()
    print header_row

    # create a variable to represent the length of the header row
    header_length = len(header_row)
    print header_length

    # create a variable to represent the datatype for the header row
    header_type = type(header_row)
    print header_type

    # loop through each item in the header_row
    for column_name in header_row:

        # log its contents
        print column_name

        # log its length
        column_name_length = len(column_name)
        print column_name_length

        # log its type
        column_name_type = type(column_name)
        print column_name_type

    # close the csv file when we're done
    csv_file.close()

open_csv_file('fdic_failed_bank_list.csv')