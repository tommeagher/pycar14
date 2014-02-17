# import modules
import csv

# write your function passing in the file name
def more_string_methods(file_name):

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

more_string_methods('fdic_failed_bank_list.csv')