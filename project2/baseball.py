import csv
import operator
import math


#First, let's see what kind of data we have to work with
def calculate_top10 (filename):
    #Open the salary csv
    salaries_object = open(filename, 'rb')

    #Make the file object usable
    salary_data = csv.reader(salaries_object)

    #Create your header row and look at what is in here
    header_row = salary_data.next()

    #Find the index of the year and player id
    print header_row

    #Check the type of the year column to see if it is a string or int
    sample_data = salary_data.next()
    print '%s is %s' % (sample_data[0], type(sample_data[0]))

    #Because we're on the first row of data, we need to 
    #return to the top before we do anything with this.
    #We do this by resetting the pointer in the original file.
    salaries_object.seek(0)

    #Arrange in descending order of salary
    #Remember that lists always keep their order!
    sorted_salaries = sorted(salary_data, key=operator.itemgetter(4), reverse=True)

    #Create a list of the top 10%
    top_percentile = len(sorted_salaries) * .10

    #Round it!
    rounded_salaries = math.floor(top_percentile)

    #We don't want decimal points (you can't have part of a player)
    #so cast to an int
    int_salaries = int(rounded_salaries)

    #You could do the above steps in one line like this:
    #int(math.floor(len(sorted_salaries * .10)))

    #Now let's create our final list, of just the highest-paid players
    cream_of_the_crop = sorted_salaries[:int_salaries]

    return cream_of_the_crop

#We are going to be working with dictionaries to make things easier
def create_player_dict(filename, cream_of_the_crop):
    #Open the csv
    salaries_object = open(filename, 'rb')

    #This time, let's use DictReader,
    #which maps the header row's values to each item in each row
    player_dict = csv.DictReader(salaries_object)

    #Create new list of only 2013 information
    #NOTE: You can't start a variable with a number, so 2013_salaries won't work
    salaries_2013 = {}

    for row in player_dict:
        #Using DictReader allows us to access rows by their column name!
       year = row["yearID"]
       if year == '2013':
           print row["playerID"]
           #Create a record for each player's ID and assign it the salary
           salaries_2013[row["playerID"]] = row["salary"]



#TODO:
#Open the master csv
#Loop over the master csv to find the player IDs in the player dict
#Add names, birth state and birth country to the dict

#TODO: Make this so we can walk a folder structure
salary_file = 'data/2013/Salaries.csv'

top10 = calculate_top10(salary_file)
create_player_dict(top10)

