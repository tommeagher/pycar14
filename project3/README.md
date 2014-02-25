# Webscraping with Python

This section covers webscraping with Python using a [get](http://www.w3schools.com/tags/ref_httpmethods.asp) request. 

To begin with we will import the [modules](http://docs.python.org/2/tutorial/modules.html) or packages we need to scrape websites. This is done with a series of import statements at the top of the file. 

```Python
import requests
from bs4 import BeautifulSoup
import csv
```

[Requests](http://requests.readthedocs.org/en/latest/) is a module used to actually retrieve the pages we want to scrape from the Internet. It, like BeautifulSoup, is not part of Python's standard library and needs to be installed using [easy_install](http://pythonhosted.org/setuptools/easy_install.html) or [pip](http://www.pip-installer.org/en/latest/). [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) is a HTML and XML parser, it is what we will be using to step through the html on a webpage and grab the data. We need to access a specific object within the BeautifulSoup module which is why we use the ```from bs4 import BeautifulSoup``` code. Finally, [csv](http://docs.python.org/2/library/csv.html) is a module designed for working with csvs - both reading and writing. We will be using it to write out the data once we parse it out of the html.

Now that we have our tools loaded into the script, we can go ahead and grab the webpage we want to scrape using requests.

```Python
r = requests.get('http://www.bls.gov/web/metro/laummtrk.htm')
```

This loads data from that url into a variable so we can work with it. Now requests returns a bunch of information about a url, but the one we are interested in is accessed through its text attribute which returns the actual html code of the page.

```Python
html = r.text
```

Now that we have the html stored in a handy variable, we can load it into BeautifulSoup's parser so we can start accessing the data. The parsed data is assigned to a variable that we will call ```soup```.

```Python
soup = BeautifulSoup(html)
```

We can start accessing text on the webpage by specifying the tags it is wrapped in. In this case we want to get at the tables in the page. So we can use BeautifulSoup's find function to isolate the tables.

```Python
table = soup.find('table')
```

That's great, but what we really want is the data within each cell - the ```<td>``` tags - of the table. Those cells are stored in rows - ```<tr>``` tags - so lets start by isolating rows using the findAll method. This method will load the results of our search into a [list](http://docs.python.org/2/tutorial/introduction.html#lists) or array that we will later loop through to further process the data. 

```Python
rows = table.findAll('tr')
```

There is some junk in the first three elements of the rows list. We can get rid of those using [slicing](http://forums.udacity.com/questions/2017002/python-101-unit-1-understanding-indices-and-slicing), keeping only the rows that we care about for the most part.

```Python
rows = rows[3:]
```

What that line of code does is take everything from the fourth row - in Python we count beginning with zero - until the end of the array and reassigning it back to the variable ```rows```. This is done using the ```rows[3:]``` syntax. The "3" to the left of the colon in the brackets actually specifies the fourth element in the array. The colon indicates that we are doing a slice. We have not put a number to the right of the colon, which tells Python to continue on until the end of the array. Specifying a number there would tell it to stop once it reaches that index number. For example ```rows[3:4]``` would return two rows.

At this point we are going to stop and take a minute to prepare the file we will write our data to.

```Python

csvfile = open("unemployment.csv","wb")

output = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

```

The first line of code above creates and opens a file named "unemployment.csv" for us. The ```"wb"``` tells Python that we want it to open the file in write mode using binary coding. Other options are read in binary ```"rb"``` and append to a file in binary ```"ab"```.

The second line of code points the csv module at the open file - telling the module that we want to create a tool that will write to this file, that this file will be a csv file with a comma delimiter and using the double quotes for a text qualifier. The last paramenter tells the csv module that we want it to only use the text qualifier where necessary.

Now that we have gotten that out of the way, we can step through the data that we have, break everything up into cells and write the data out to the csv file in a nice, easy to read format. We are going to start with a [for](http://learnpythonthehardway.org/book/ex32.html) loop. A for loop repeats a set task or tasks on each element in the array, stopping once it reaches the end of the array. It starts like this:

```Python
for row in rows:
```

The variable ```row``` refers to the specific element we are working on in the array. The colon tells Python to begin working on that item with the code located below.

```Python
for row in rows:
    cells = row.findAll('td')
    if cells[1].text == "":
        continue
    rank = cells[0].text.strip()
    geography = cells[1].text.strip()
    rate = cells[2].text.strip()
    output.writerow([rank,geography,rate])
```

There is a lot going on here and we will take it step-by-step, but first a matter of formatting. Once you start a for loop - or any other loop for that matter - Python requires code to be indented in order for it to be included in the loop. Good coding convention says that indent is four spaces (not a tab). Any indented code will be executed as part of that loop, unindented code is outside the loop and will signify its end.

Now the first line of the indented code, ```cells = row.findAll('td')``` is splitting the current row up into another list, this one of the individual cells of that table. This is where we are starting to actually get at our data finally. But there is a problem. Not all rows contain data, some of them are blank and we want to discard those rows. To do so we build in a conditional - an [if statement](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html). 

```Python 
    if cells[1].text == "":
```

A few things going on here. We are basically asking if the text value of the second cell in the row is blank, do something. The variable ```cells[1]``` refers to the second element in the ```cells``` list by using the [1] notation - remember that Python is zero-based, the first cell would actually be ```cells[0]```. By placing the numerical index in brackets, we are telling Python to only access the value at that position. 

Additionally, we are checking the value in the second cell of the row because the listing for the United States does not have a ranking in the first cell and is blank. We are signifying the blank value using a pair of double quotes with nothing in between them. The double equal signs are how we make a comparison. A single equals sign would assign a value to that variable instead of checking the value. Lastly, the colon tells Python that the next line of code will contain what we want to happen when the condition is true. We can also add ```elif``` (else if) and ```else``` if we had multiple conditions or responses that we wanted to test or execute, but that is not the case here.

The next line is indented, just as we did with the for loop above and for exactly the same reason. Indented lines of code tell Python that those lines belong to the conditional statement. In this case it is a single word ```continue```. [Continue](http://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) tells Python to skip the rest of the code in the loop and then move onto the next element in the list we are looping through as if nothing had happened. This is effectively skipping the blank rows. 

With those rows skipped, we can continue on to working with the rows that we care about. Note that the following lines of code are indented so they remain a part of the for loop, but not double indented so they are excluded from the if statement above. We are assigning values of the cells to variables named in a way that makes sense to us, so we can easily tell what we are working with.

```Python
    rank = cells[0].text.strip()
    geography = cells[1].text.strip()
    rate = cells[2].text.strip()
```

By now you should recognize the notation - we refer to a specific cell by its numerical index enclosed in brackets after the variable name. Next we grab the actual text within the cell by calling ```.text``` on it. Finally we introduce a new step - ```.strip()```. [Strip](http://www.tutorialspoint.com/python/string_strip.htm) removes any excess characters specified within the parentheses from the text. Since we left the parenthese empty, ```strip()``` will remove extra whitespace. This process is executed for each of the three cells which are then assigned to their respective variables. Now it is time to write those cells out to our output file in a csv format.

```Python
    output.writerow([rank,geography,rate])
 ```

 In order to do this we tell the csv writer that we created that we want it to write a row out to our file. This is done simply with ```output.writerow```. We put the value we want to write out within the parentheses. Now sense this is a csv, the writer will want multiple items it can write out separated by a comma. 

 To do this we create a list of our own within the parentheses - ```[rank,geography,rate] ```. Lists are enclosed in square brackets and each item is separated by a column. Since the items we want to put into the csv document are stored in variables, we simply list the variable names without any quotation marks. If we wanted to write out actual values, they would be enclosed in quotation marks like ```["Heather","Tom","Chris"]```.

 At this point we have accessed the website, parsed the html, scraped out the data and written it out to a file. The final step is to close the output file to prevent any further changes and free up memory dedicated to keeping it open.

 ```Python
 csvfile.close()
 ```

 This is an important step, you can lose your work by leaving this file open or by opening it again in write mode accidentally. Also notice that this line is not indented at all, it is only carried out after the for loop finishes iterating through all the rows of the html table you are scraping.