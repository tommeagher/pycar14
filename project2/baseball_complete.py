# Imports go here
import csv
import math
from pprint import pprint

# Dict syntax example
my_deets = {'name': 'Heather', 'gender': 'f' }
# Alternate dict creation syntax
my_deets_alt = dict(name="Heather", gender="f")
# Dict contents can be copied
copy_of_my_deets = dict(my_deets)
# Creating a new dict that includes the values of an existing dict
deets_plus_pet = dict(my_deets, pet="Rascal the horse")
# Add two dicts together
deets_plus_job = dict(my_deets, **{'employer': 'Northwestern University', 'boss': 'Joe Germuska'})
# Adding two dicts that are both variables
job_deets = {'employer': 'Northwestern University', 'boss': 'Joe Germuska'}
deets_plus_job = dict(my_deets, **job_deets)


# File with baseball players' salaries
salary_file = 'data/2014/Salaries.csv'

# File with player details
master_file = 'data/2014/Master.csv'


# First, let's see what kind of data we have to work with
def explore_data(filename):
    # Open the file
    with open(filename, 'rb') as file:
        # Print out the header row
        header_row = file.next()
        print header_row
        # Print out a row of sample data
        sample_data = file.next()
        print sample_data
        # Split sample data on comma so we can loop over it
        items = sample_data.split(',')
        # Check to see what type each item is
        for item in items:
            print '%s is type %s' % (item, type(item))


# Checks to see if the passed value can be converted to an integer. If not, return original value.
def str_to_int(value):
    try:
        return int(value)
    except:
        return value


# Returns the passed row as key/value pairs
def check_for_ints(row):
    return {key: str_to_int(value) for key, value in row.iteritems()}


# Create a basic file reader
def read_file(filename):
    with open(filename, 'rb') as file:
        reader = csv.DictReader(file)
        # Because the salaries come through as strings, cast to ints before we sort
        return [check_for_ints(row) for row in reader]


# Create dicts
def create_keyed_data(filename, key):
    simple_data = read_file(filename)
    keyed_data = {}
    for row in simple_data:
        keyed_data[row["playerID"]] = row
    return keyed_data


# Join dicts
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

salaries = create_keyed_data(salary_file, "playerID")
master = create_keyed_data(master_file, "playerID")
player_data = join_dicts(salaries, master)

write_file('data/2014/highest_paid_players.csv', get_top_players(player_data))
