import csv

#TODO: Make this so we can walk a folder structure
SALARIES_FILE = 'data/2013/Salaries.csv'


#First, let's see what kind of data we have to work with
def explore_salary_csv(filename):
    #Open the salary csv
    salaries_object = open(SALARIES_FILE, 'rb')

    #Make the file object usable
    salary_data = csv.reader(salaries_object)

    #Create your header row
    header_row = salary_data.next()

    #Find the index of the year and player id
    print header_row

    #Check the type of the year column to see if it is a string or int
    sample_data = salary_data.next()
    print '%s is %s' % (sample_data[0], type(sample_data[0]))


#We are going to be working with dictionaries to make things easier
def use_dicts(filename):
#Open the csv
salaries_object = open(SALARIES_FILE, 'rb')

#This time, let's use DictReader,
#which maps the header row's values to each item in each row
salary_data = csv.DictReader(salaries_object)



#Create new list of only 2013 information
#NOTE: You can't start a variable with a number, so 2013_salaries won't work
salaries_2013 = {}

for row in salary_data:
    #Using DictReader allows us to access rows by their column name!
     year = row["yearID"]
     if year == '2013':
         print row
#Arrange in descending order of salary
#Create a dict with salaries and playerIDs of the top 10%

#Open the master csv
#Loop over the master csv to find the player IDs in the player dict
#Add names, birth state and birth country to the dict



for row in salary_data:
    for item in row:
        print '%s is type %s' % (item, type(item))
