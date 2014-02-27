import csv
import operator
import math
from pprint import pprint


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
    cream_of_the_crop = []

    #We only need the player IDs right now.
    for index, row in enumerate(sorted_salaries):
        if index > 0 and index <= int_salaries:
            cream_of_the_crop.append(row[3])

    return cream_of_the_crop


#We are going to be working with dictionaries to make things easier
def create_salary_dict(filename, cream_of_the_crop):
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
           #Create a record for each player's ID and assign it the salary
           salaries_2013[row["playerID"]] = row["salary"]

    #Now we can reference the salary of any player whose ID we know.
    #But we only want those who were in the top 10% of all time.
    #Create a new dict to hold just the top players from 2013
    top_salaries_2013 = {}

    #Let's compare our player dict with the list of all-time 
    #high salaries we made in the first function.
    #(You could combine this step with the DictReader step above.)
    for player in cream_of_the_crop:
        #Check for the presence of a key that matches the playerID in salaries_2013
        if player in salaries_2013:
            top_salaries_2013[player] = { "salary": salaries_2013[player] }

    return top_salaries_2013


def add_player_stats(top_salaries_dict, master_file):
    #Open the master csv
    master_object = open(master_file, 'rb')

    #Read the file
    master_data = csv.DictReader(master_object)

    #Let's look at one record of the master data to get the headers
    print master_data.next()

    #That's a little hard to read, isn't it? Try prettyprint instead.
    pprint(master_data.next())

    #Reset the generator and skip the header row
    master_object.seek(0)
    master_data.next()

    #Create a dict of the master file with DictReader
    master_dict = {}

    #Assemble the troops
    for row in master_data:
        master_dict[row["playerID"]] = {
            "first_name": row["nameFirst"],
            "given_name": row["nameGiven"],
            "last_name": row["nameLast"],
            "height": row["height"],
            "weight": row["weight"],
            "birth_city": row["birthCity"],
            "birth_state": row["birthState"],
            "birth_country": row["birthCountry"],
            "birthdate": '%s-%s-%s' %(row["birthDay"], row["birthMonth"], row["birthYear"]),
            "death_city": row["deathCity"],
            "death_state": row["deathState"],
            "death_country": row["deathCountry"],
            "deathdate": '%s-%s-%s' %(row["deathDay"], row["deathMonth"], row["deathYear"]),
            "bats": row["bats"],
            "throws": row["throws"],
            "debut": row["debut"],
            "final_game": row["finalGame"]
        }

    #Loop over the top salaries dict to find the player IDs in the master dict
    #We could also loop over the master dict to find which of those exist
    #in the top salaries dict, but that would be less efficient.
    #When you loop over a dict, you only have access to the keys.
    #To access the values, we need .iteritems()
    #Remember the key is the player ID and the value is the salary.
    #Typically, when iterating over a dict, the syntax is:
    #for key, value in my_dict.iteritems():
    #For clarity, we will use the header row values instead.


    #Add names, birth state and birth country to the dict
    for playerID, salary in top_salaries_dict.iteritems():
        top_salaries_dict.update({ playerID: {
            'first_name':  master_dict[playerID]["first_name"],
            'last_name': master_dict[playerID]["last_name"],
            'birth_state': master_dict[playerID]["birth_state"],
            'birth_country': master_dict[playerID]["birth_country"]}
        })

    return top_salaries_dict

salary_file = 'data/2013/Salaries.csv'

#TODO: Make this so we can walk a folder structure
master_file = 'data/2013/Master.csv'

top10 = calculate_top10(salary_file)
top_salaries_dict = create_salary_dict(top10)
final_file = add_player_stats(top_salaries_dict, master_file)

#write to a file
