# import modules
import csv

# write your function passing in the file name
def output_rows_from(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # loop through each row in the object
    for row in csv_data:

        # output the type
        print type(row)

        # output the length of the row
        print len(row)

        # output the contents
        print row

    # close the csv file when we're done
    csv_file.close()

output_rows_from('fdic_failed_bank_list.csv')