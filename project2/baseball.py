# Imports go here

# Dict syntax example
# Alternate dict creation syntax
# Dict contents can be copied
# Creating a new dict that includes the values of an existing dict
# Add two dicts together
# Adding two dicts that are both variables

# File with baseball players' salaries
salary_file = 'data/2016/Salaries.csv'

# File with player details
master_file = 'data/2016/Master.csv'


# First, let's see what kind of data we have to work with
    # Open the file
        # Print out the header row
        # Print out a row of sample data
        # Split sample data on comma so we can loop over it
        # Check to see what type each item is


# Step 1.3: Convert numbers to ints
    # Try to convert the passed value to an integer
    # If not, return original value.


# Step 1.2 Return the passed row as key/value pairs
    # Each row contains a key/value pair, so get it with iteritems
    # Check each key to see if it can be converted to an int


# Step 1.1: Create a basic file reader
        # Open with DictReader so that we can use the header row as keys
        # Because the salaries come through as strings, cast to ints before we sort


# Step 1: Create dicts from data
    # Read file into a variable
    # Create a new dict object
    # Add each row of data to the dict
    # Return the data


# Step 2: Join two dicts on a shared key
    # Get the unique keys present in both dicts
    # Create a new dict that will contain all data
    # Loop over keys
        # Create a new key/value pair from the values present in both dicts.
            # Make value of key in merged_data equal the corresponding
            # keyed value from each dict.
            # NOTE: If the value is present in both, the second value will override the first.
            # If the value is present in one but not the other, an exception will be thrown


# Step 3: Turn the player data into a list of the highest paid players
# NOTE: This is simplified as an example and not reliable for cleaning real data.
    # NOTE: Dicts are unordered and do not retain order if sorted.
    # Sort data by salary and assign the reverse-sorted list to a variable
    # Figure out what 10% of the number of players is, rounded
    # Return just the slice of the list that includes the top 10%


# Step 4: Writes the cleaned data back to a file
    # Open your new file as writeable
        # Make sure that the data variable has content so you don't write a blank file
        # Create a DictWriter
        # Write the header of the file
        # Write each key/value pair as a row in the new CSV


salaries = create_keyed_data(salary_file, "playerID")
master = create_keyed_data(master_file, "playerID")
player_data = join_dicts(salaries, master)

write_file('data/2014/highest_paid_players.csv', get_top_players(player_data))
