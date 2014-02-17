# import modules
import csv

# write your function passing in the file name
def output_first_csv_row(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # create a variable to represent the header row
    header_row = csv_data.next()

    # let's get the first row of data
    data_row = csv_data.next()

    # let's create a varaible off the bat to isolate
    # the integer that is the zip code
    my_integer = data_row[3]

    # let's output the value
    print my_integer

    # let's get the length of the integer
    print len(my_integer)

    # for kicks let's multiply zipcode by 2. we should get 68592
    print my_integer * 2

    # let's make sure this is an integer
    # because its not an integer, when we tried to double it, python simply repeated the string
    print type(my_integer)

    # let's convert the string to an integer
    my_integer = int(my_integer)
    print type(my_integer)

    # now let's try some math

    # multiplication
    print my_integer * 2

    # division
    print my_integer / 2

    # addition
    print my_integer + 1000

    # subtraction
    print my_integer - 1000

    # order of operations
    print (my_integer*2+56)/100

    # close the csv file when we're done
    csv_file.close()

output_first_csv_row('fdic_failed_bank_list.csv')