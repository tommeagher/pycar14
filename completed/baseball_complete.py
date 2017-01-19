# Dict syntax example
hero = {'name':'Lancelot', 'fav_color':'blue'}

# Alternate dict creation syntax
hero_alt = dict(name='Lancelot',fav_color='blue')

# Dict contents can be copied
hero_copy = dict(hero)

# Creating a new dict that includes the values of an existing dict
hero_plus_mission = dict(hero, mission="find the Holy Grail")
hero_plus_mission = dict(hero, **{'mission':'find the Holy Grail', } )

# Add two dicts together with the '**' operator
hero_plus_companion = dict(hero, **{'companion':'Brave ser Robin'} )

# Adding two dicts that are both variables
hero_extra = dict(hero, **hero_plus_mission )

# Imports go here
import csv

# File with baseball players' salaries
salary_file = 'data/2016/Salaries.csv'

# File with player details
master_file = 'data/2016/Master.csv'

# First, let's see what kind of data we have to work with

# Open the salary file using 'with' syntax
with open(salary_file, 'rb') as csv_file:
    # Read the csv file
    reader = csv.reader(csv_file)
    # put first row into variable 'header_row'
    header_row = reader.next()
    # Print out the header row
    print(header_row)
    # put second row into variable 'sample_data'
    sample_data = reader.next()
    # Print out a row of sample data
    print sample_data
    # print out the contents and type of the cells in variable 'sample data'
    for item in sample_data:
        print item, type(item)
    # Check to see what type each item is with str.format()


# We can change 'salary_file' to 'master_file' above to do the same for the other file
# How could this be modified so that it's a function we could use on any CSV?

# define a function 'explore_data' that will take one argument 'filename')
def explore_data(filename):
    # the same as above. We don't need to use 'return' because we are just printing variables for us to see
    # we do need to use 'return' if we want Python to do something with the output of the function
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        header_row = reader.next()
        print(header_row)
        sample_data = reader.next()
        print sample_data
        for item in sample_data:
            print item, type(item)

# call the function on 'master file'
explore_data(master_file)

# Mission: join the two csv's. They both contain the "playerID" column


# Step 1: Create a file reader function that converts strings to integers
def read_file(filename):

    # Open like above, but make a DictReader object instead, so each row of data
    # is a dictionary we'll store as items in a list called 'file_row'
    with open(filename, 'rb') as csv_file:
        reader = csv.DictReader(csv_file)
        # create an empty dictionary that will hold the fixed data
        file_rows = {}

        for row in reader:
            # create an empty dictionary that will hold the fixed row and be rewritten every time
            fixed_row = {}
            for cell in row:
                # try to convert the cell into an integer
                try:
                    fixed_row[cell] = int(row[cell])
                # if the cell can not be converted, just leave it be
                except ValueError:
                    fixed_row[cell] = row[cell]

            # after the row is fixed, put it into the 'file_rows' dictionary.
            # use the 'playerID' as the key (as this is in both of the files we want to join)
            file_rows[fixed_row["playerID"]] = fixed_row

    # return the dictionary of dictionaries
    return file_rows

fixed_master = read_file(master_file)
fixed_salaries = read_file(salary_file)

# Step 2: Join two dicts on a shared key
def join_dicts(dict1,dict2):
    # Get the unique keys present in both dicts
    keys = set(dict1.keys() + dict2.keys())
    # Create a new list that will contain all data
    merged_data = []

    # Loop over keys
    for key in keys:
        try:
            # Create a new key/value pair from the values present in both dicts.
            # NOTE: If the value is present in both, the second value will override the first.
            merged_data.append(dict(dict1[key], **dict2[key]))
        # If the value is present in one but not the other, an exception will be thrown
        except KeyError:
            continue
    
    return merged_data

# Join the data with the join_dict() function and send it to a new variable
merged = join_dicts(fixed_master,fixed_salaries)

# Step 3: Writes the cleaned data back to a CSV
# Open your new file as writeable
with open("merged.csv", 'wb') as outputfile:

    # Create the header of the file
    header = merged[0].keys()
    # Create a DictWriter
    writer = csv.DictWriter(outputfile, fieldnames = header)
    # Write the header of the file
    writer.writeheader()
    # Write each key/value pair as a row in the new CSV
    for row in merged:
        writer.writerow(row)
