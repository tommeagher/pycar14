# import modules
import csv

# write your function passing in the file name
def basic_string_methods(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # create a variable to represent the header row
    header_row = csv_data.next()

    # from the last lesson we know the variable header_row refers to a list
    # let's isolate the string that is 'Acquiring Institution'
    print header_row

    # we'll do this by isolating in the list what is know as the index of the string
    print header_row[4]

    # let's make sure this is a string
    print type(header_row[4])

    # let's get the length of the string
    print len(header_row[4])

    # create a variable to hold our string
    my_string = header_row[4]

    # let's see how string subscripting works
    # let's print the third characters
    print my_string[2]

    # let's print the first five characters
    print my_string[:5]

    # let's print everything after the first five characters
    print my_string[5:]

    # let's capitalize the first letter in the string
    print my_string.capitalize()

    # let's lowercase the string
    print my_string.lower()

    # let's uppercase the string
    print my_string.upper()

    # close the csv file when we're done
    csv_file.close()

basic_string_methods('fdic_failed_bank_list.csv')