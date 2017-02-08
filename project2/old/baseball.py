# Dict syntax example

# Alternate dict creation syntax

# Dict contents can be copied

# Creating a new dict that includes the values of an existing dict


# Add two dicts together with the '**' operator

# Adding two dicts that are both variables

# Imports go here

# File with baseball players' salaries

# File with player details

# First, let's see what kind of data we have to work with

# Open the salary file using 'with' syntax

    # Read the csv file

    # put first row into variable 'header_row'

    # Print out the header row

    # put second row into variable 'sample_data'

    # Print out a row of sample data

    # print out the contents and type of the cells in variable 'sample data'

    # Check to see what type each item is with str.format()

# We can change 'salary_file' to 'master_file' above to do the same for the other file
# How could this be modified so that it's a function we could use on any CSV?

# define a function 'explore_data' that will take one argument 'filename')
    # the same as above. We don't need to use 'return' because we are just printing variables for us to see
    # we do need to use 'return' if we want Python to do something with the output of the function

# call the function on 'master file'

# Mission: join the two csv's. They both contain the "playerID" column

# Step 1: Create a file reader function that converts strings to integers
    # Open like above, but make a DictReader object instead, so each row of data
    # is a dictionary we'll store as items in a list called 'file_row'

        # create an empty dictionary that will hold the fixed data

            # create an empty dictionary that will hold the fixed row and be rewritten every time

                # try to convert the cell into an integer

                # if the cell can not be converted, just leave it be

            # after the row is fixed, put it into the 'file_rows' dictionary.

            # use the 'playerID' as the key (as this is in both of the files we want to join)

    # return the dictionary of dictionaries

# Step 2: Join two dicts on a shared key

    # Get the unique keys present in both dicts

    # Create a new list that will contain all data

    # Loop over keys

            # Create a new key/value pair from the values present in both dicts.
            # NOTE: If the value is present in both, the second value will override the first.

        # If the value is present in one but not the other, an exception will be thrown

# Join the data with the join_dict() function and send it to a new variable

# Step 3: Writes the cleaned data back to a CSV

# Open your new file as writeable

    # Create the header of the file

    # Create a DictWriter

    # Write the header of the file

    # Write each key/value pair as a row in the new CSV
