# Imports go here
import csv
import math

# Dict syntax example
my_deets = {'name': 'Heather', 'gender': 'f'}

# Alternate dict creation syntax
my_deets_alt = dict(name="Heather", gender="f")

# Dict contents can be copied
deets_copy = dict(my_deets)

# Creating a new dict that includes the values of an existing dict
deets_plus_pet = dict(my_deets, pet="Rascal the horse")

# Add two dicts together with the '**' operator
deets_plus_job = dict(my_deets, **{'employer': 'Northwestern University', 'boss': 'Joe Germuska'})

# Adding two dicts that are both variables
job_deets = {'employer': 'Northwestern University', 'boss': 'Joe Germuska'}
deets_plus_job = dict(my_deets, **job_deets)

# File with baseball players' salaries
salary_file = 'data/2016/Salaries.csv'

# File with player details
master_file = 'data/2016/Master.csv'


# First, let's see what kind of data we have to work with

# Open the salary file using 'with' syntax
with open(master_file, 'rb') as csv_file:
    # Print out the header row
    reader = csv.reader(csv_file)
    header_row = reader.next()
    print header_row
    # Print out a row of sample data
    sample_data = reader.next()
    print sample_data
    # Check to see what type each item is with str.format()
    for item in sample_data:
        print '{0} is type {1}'.format(item, type(item))

# We can change 'salary_file' to 'master_file' above to do the same for the other file
# How could this be modified so that it's a function we could use on any CSV?
def explore_data(file):
    with open(file, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        header_row = reader.next()
        print header_row
        sample_data = reader.next()
        print sample_data
        for item in sample_data:
            print '{0} is type {1}'.format(item, type(item))

# Try modifying the code above to make it a function called 'explore_data' and
# run it on the salary file CSV
explore_data(salary_file)


# Create a file reader function that converts strings to integers
def read_file(filename):
    # Open like above, but make a DictReader object instead, so each row of data
    # is a dictionary we'll store as items in a list called 'file_rows'
    with open(filename, 'rb') as csv_file:
        reader = csv.DictReader(csv_file)
        file_rows = []
        # Step through each row in the data
        for row in reader:
            fixed_row = {}
            # Step through each data point in the row
            for element in row:
                # Try to make it an integer; if there's an error, it will remain
                # a string.
                try:
                    fixed_row[element] = int(row[element])
                except:
                    fixed_row[element] = row[element]
            file_rows.append(fixed_row)
        return file_rows


# Create a function that converts our list of dicts into something that can be
# joined: a dict of dicts
def create_keyed_data(filename, key):
    simple_data = read_file(filename)
    keyed_data = {}
    # We need the key in this new dict to point to the row of data
    for row in simple_data:
        keyed_data[row[key]] = row
    return keyed_data


# Join the dicts together where they share a common key
def join_dicts(dict1, dict2):
    keys = set(dict1.keys() + dict2.keys())
    merged_data = []
    for key in keys:
        try:
            # Equivalent to copying the values of two dicts
            # The double asterisk just expands the values
            merged_data.append(dict(dict1[key], **dict2[key]))
        except:
            pass
    return merged_data

# Turn the player data into a list of the highest paid players
# NOTE: This is simplified as an example and not reliable for cleaning real data.
def get_top_players(player_data):
    sorted_salaries = sorted(player_data, key=lambda player: player["salary"], reverse=True)
    # NOTE In "real life", you'd need to account for the 10% figure potentially ending in the middle
    # of a block of players who all made the same salary.
    player_count = int(math.floor(len(sorted_salaries) * .10))
    return sorted_salaries[0:player_count + 1]


# Writes the cleaned data back to a file
def write_file(filename, data):
    with open(filename, 'wb') as file:
        assert(data)
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for line in data:
            writer.writerow(line)

# Finally, let's invoke these functions to make the top players CSV

# Make variables to hold keyed data from the master file and the salary file
salaries = create_keyed_data(salary_file, "playerID")
master = create_keyed_data(master_file, "playerID")

# Join the data with the join_dict() function and send it to a new variable
player_data = join_dicts(salaries, master)

# Write the results of get_top_players() to a new CSV
write_file('data/2016/highest_paid_players.csv', get_top_players(player_data))
