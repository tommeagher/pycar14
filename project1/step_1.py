# import modules
import csv

# write your first function passing in the file name
def open_csv_file(file_name):

    # use the csv module to open the csv file
    with open(file_name, 'rb') as csv_file:

        # create the object that represents the data in the csv file
        csv_data = csv.reader(csv_file)

        # output that object to the terminal
        print csv_data

    # close the csv file when we're done
    csv_file.close()

# run the function when you run the script in the terminal
if __name__ == '__main__':
    open_csv_file('fdic_failed_bank_list.csv')