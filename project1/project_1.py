# import modules
import csv

FILE_NAME = 'fdic_failed_bank_list.csv'

# write a function to open a csv file
def open_csv_file(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # output that object to the terminal
    print csv_data

    # close the csv file when we're done
    csv_file.close()

### ###

# write a function to count the number of rows in a csv file
def count_csv_rows(file_name):

    # create a variable to iterate each row and count the number of lines
    number_of_rows = sum(1 for line in open(file_name))

    # output the number of lines
    print number_of_rows

### ###

# write a function to print each row from a csv file
# and get its length and if it's a string or an integer
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

### ###

# write a function to output the first row of a csv file
# and get the column names
def output_first_csv_row(file_name):

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

### ###

# write a function to do some exploring with strings
def working_with_strings(file_name):

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

### ###

# write a function to do some more exploring with strings
def doing_more_with_strings(file_name):

    # open the csv
    csv_file = open(file_name, 'rb')

    # create the object that represents the data in the csv file
    csv_data = csv.reader(csv_file)

    # create a variable to represent the header row
    header_row = csv_data.next()

    # from the last lesson we know the variable header_row refers to a list
    # let's isolate the string that is 'Acquiring Institution'
    print header_row

    # create a variable to hold our string
    my_string = header_row[4]

    # let's evaluate the uppercase version is equal to the lowercase version
    print my_string.upper() == my_string.lower()

    # let's remove the space that is present in the string
    print my_string.replace(' ', '')

    # let's change the space to an underscore
    print my_string.replace(' ', '_')

    # let's look at the strip method by giving it a value
    print my_string.strip('Acquiring')

    # let's look at what the strip method does to the ouput of above
    print my_string.strip('Acquiring').strip()

    # let's try to split the string on the space
    print my_string.split(' ')

    # let's get the datatype for the thing we just created
    # first lets create a variable to hold this string
    my_split_string = my_string.split(' ')

    # then let's get the type
    print type(my_split_string)

    # because it's a list, we can again get a specfic item by it's index
    # and we're back to where we started
    print my_split_string[0]

    # for the final item let's use the length of the list and lowercase the two strings we created to create a sentence
    print 'I made %d strings from a list I created. They are: %s & %s' % (len(my_split_string), my_split_string[0].lower(), my_split_string[1].lower())

    # close the csv file when we're done
    csv_file.close()

### ###

# write a function to do some exploring with integers
def working_with_integers(file_name):

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

# run the function when you run the script in the terminal
open_csv_file(FILE_NAME)
#count_csv_rows(FILE_NAME)
#output_rows_from(FILE_NAME)
#output_first_csv_row(FILE_NAME)
#basic_string_methods(FILE_NAME)
#more_string_methods(FILE_NAME)
#working_with_integers(FILE_NAME)