# import built-in python modules
# we'll want to access csv files and download files
import csv
import urllib

# we're going to download a csv file
# what should we name it
file_name = "banklist.csv"

# use urllib.urlretrieve() to download the csv file from a url and save it to a directory
# csv link found at https://www.fdic.gov/bank/individual/failed/banklist.html
target_file = urllib.urlretrieve("http://www.fdic.gov/bank/individual/failed/banklist.csv", file_name)

# open the file to write
output_file = open('georgia_banks.csv', 'wb')

# create the writer object
writer = csv.writer(output_file, delimiter=',')

# open the csv file
with open(file_name, "rb") as file:

    # use python's csv reader to access the contents
    # and create an object that represents the data
    csv_data = csv.reader(file)

    # write our header row to the output csv
    header_row = csv_data.next()
    writer.writerow(header_row)

    # loop through each row of the csv
    for row in csv_data:
        # if the state field equals georgia
        if row[2] == "GA":
            # write the row to the new csv file
            writer.writerow(row)
            print row
        # otherwise continue on
        else:
            continue

# close our new file
output_file.close()
