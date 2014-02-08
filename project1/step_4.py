# import modules
import csv, logging

logging.basicConfig(format='\033[1;36m%(levelname)s:\033[0;37m %(message)s', level=logging.DEBUG)

# write your function passing in the file name
def open_csv_file(file_name):

    # use the csv module to open the csv file
    with open(file_name, 'rb') as csv_file:

        # create the object that represents the data in the csv file
        csv_data = csv.reader(csv_file)

        # create a variable to represent the header row
        header_row = csv_data.next()
        logging.debug(header_row)

        # create a variable to represent the length of the header row
        header_length = len(header_row)
        logging.debug(header_length)

        # create a variable to represent the datatype for the header row
        header_type = type(header_row)
        logging.debug(header_type)

        # loop through each item in the header_row
        for column_name in header_row:

            # log its contents
            logging.debug(column_name)

            # log its length
            column_name_length = len(column_name)
            logging.debug(column_name_length)

            # log its type
            column_name_type = type(column_name)
            logging.debug(column_name_type)

    # close the csv file when we're done
    csv_file.close()

# run the function when you run the script in the terminal
if __name__ == '__main__':
    open_csv_file('fdic_failed_bank_list.csv')