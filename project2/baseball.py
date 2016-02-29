# Imports go here


# Dict syntax example


# Alternate dict creation syntax


# Dict contents can be copied


# Creating a new dict that includes the values of an existing dict


# Add two dicts together with the '**' operator


# Adding two dicts that are both variables


# File with baseball players' salaries
# 'data/2016/Salaries.csv'

# File with player details
# 'data/2016/Master.csv'


# First, let's see what kind of data we have to work with

# Open the salary file using 'with' syntax

    # Print out the header row

    # Print out a row of sample data

    # Check to see what type each item is with str.format()


# We can change 'salary_file' to 'master_file' above to do the same for the other file
# How could this be modified so that it's a function we could use on any CSV?


# Try modifying the code above to make it a function called 'explore_data' and
# run it on the salary file CSV


# Step 1: Create a file reader function that converts strings to integers

    # Open like above, but make a DictReader object instead, so each row of data
    # is a dictionary we'll store as items in a list called 'file_rows'


# Step 2: Create a function that converts our list of dicts into something that can be
# joined: a dict of dicts

    # Read file into a variable
    # Create a new dict object
    # Add each row of data to the dict
    # Return the data


# Step 3: Join two dicts on a shared key
    # Get the unique keys present in both dicts
    # Create a new dict that will contain all data
    # Loop over keys
        # Create a new key/value pair from the values present in both dicts.
            # Make value of key in merged_data equal the corresponding
            # keyed value from each dict.
            # NOTE: If the value is present in both, the second value will override the first.
            # If the value is present in one but not the other, an exception will be thrown


# Step 4: Turn the player data into a list of the highest paid players
# NOTE: This is simplified as an example and not reliable for cleaning real data.
    # NOTE: Dicts are unordered and do not retain order if sorted.
    # Sort data by salary and assign the reverse-sorted list to a variable
    # Figure out what 10% of the number of players is, rounded
    # Return just the slice of the list that includes the top 10%


# Step 5: Writes the cleaned data back to a file
    # Open your new file as writeable
        # Make sure that the data variable has content so you don't write a blank file
        # Create a DictWriter
        # Write the header of the file
        # Write each key/value pair as a row in the new CSV

# Finally, let's invoke these functions to make the top players CSV

# Make variables to hold keyed data from the master file and the salary file


# Join the data with the join_dict() function and send it to a new variable

# Write the results of get_top_players() to a new CSV
