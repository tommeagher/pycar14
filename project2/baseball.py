#imports

#First, let's see what kind of data we have to work with

    #Open the salary csv
   
    #Make the file object usable
   
    #Create your header row and look at what is in here
   
    #Find the index of the year and player id

    #Check the type of the year column to see if it is a string or int

    #Because we're on the first row of data, we need to 
    #return to the top before we do anything with this.
    #We do this by resetting the pointer in the original file.

    #Arrange in descending order of salary
    #Remember that lists always keep their order!

    #Create a list of the top 10%

    #Round it!

    #We don't want decimal points (you can't have part of a player)
    #so cast to an int

    #You could do the above steps in one line like this:
    #int(math.floor(len(sorted_salaries * .10)))

    #Now let's create our final list, of just the highest-paid players

    #We only need the player IDs right now.


#We are going to be working with dictionaries to make things easier

    #Open the csv

    #This time, let's use DictReader,
    #which maps the header row's values to each item in each row

    #Create new list of only 2013 information
    #NOTE: You can't start a variable with a number, so 2013_salaries won't work

        #Using DictReader allows us to access rows by their column name!

           #Create a record for each player's ID and assign it the salary

    #Now we can reference the salary of any player whose ID we know.
    #But we only want those who were in the top 10% of all time.
    #Create a new dict to hold just the top players from 2013


    #Let's compare our player dict with the list of all-time 
    #high salaries we made in the first function.
    #(You could combine this step with the DictReader step above.)

        #Check for the presence of a key that matches the playerID in salaries_2013


#new function

    #Open the master csv

    #Read the file

    #Let's look at one record of the master data to get the headers

    #That's a little hard to read, isn't it? Try prettyprint instead.

    #Reset the generator and skip the header row

    #Create a dict of the master file with DictReader

    #Assemble the troops

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


#write to a file
