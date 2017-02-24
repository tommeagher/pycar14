# Webscraping with Python

This section covers scraping pages on the Web with Python using a [get](http://www.w3schools.com/tags/ref_httpmethods.asp) request. 

To begin with, we will import the [modules](http://docs.python.org/3/tutorial/modules.html) or packages we need to scrape websites. This is done with a series of import statements at the top of the file. 

```Python
import requests
from bs4 import BeautifulSoup
import csv
```

[Requests](http://requests.readthedocs.org/en/latest/) is a module used to retrieve the pages we want to scrape from the Internet. It, like BeautifulSoup, is not part of Python's standard library and needs to be installed using [easy_install](http://pythonhosted.org/setuptools/easy_install.html) or [pip](http://www.pip-installer.org/en/latest/). [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) is a HTML and XML parser, it is what we will be using to step through the html on a webpage and grab the data. We need to access a specific object within the BeautifulSoup module which is why we use the ```from bs4 import BeautifulSoup``` code. Finally, [csv](http://docs.python.org/2/library/csv.html) is a module designed for working with csvs - both reading and writing. We will be using it to write out the data once we parse it out of the html.

Now that we have our tools loaded into the script, we can go ahead and grab the webpage we want to scrape using requests.

```Python
r = requests.get('http://www.rentrak.com/section/movies_and_tv_everywhere/top_entertainment_rankings.html')
```

This loads data from that url into a variable so we can work with it. Now requests returns a bunch of information about a url, but the one we are interested in is accessed through its text attribute which returns the actual html code of the page.

```Python
html = r.text
```

Now that we have the html stored in a handy variable, we can load it into BeautifulSoup's parser so we can start accessing the data. The parsed data is assigned to a variable that we will call ```soup```.

```Python
soup = BeautifulSoup(html, "html.parser")
```

We can start accessing text on the webpage by specifying the tags it is wrapped in. In this case we want to get at the tables in the page. So we can use BeautifulSoup's find function to isolate the tables. Since there are multiple tables and we want only one, we will add a parameter where it will only find the table with the class of 'entChartTable.'

```Python
table = soup.find('table')
```

That's great, but what we really want is the data within each cell - the ```<td>``` tags - of the table. Those cells are stored in rows - ```<tr>``` tags - so lets start by isolating rows using the find_all method. This method will load the results of our search into a [list](http://docs.python.org/2/tutorial/introduction.html#lists) or array that we will later loop through to further process the data. 

```Python
rows = table.find_all('tr')
```

There are headers in this table with no actual data. We can get rid of those using [slicing](http://forums.udacity.com/questions/2017002/python-101-unit-1-understanding-indices-and-slicing), keeping only the rows that we care about for the most part.

```Python
rows = rows[2:]
```

What that line of code does is take everything from the fourth row - in Python we count beginning with zero - until the end of the array and reassigning it back to the variable ```rows```. This is done using the ```rows[3:]``` syntax. The "3" to the left of the colon in the brackets actually specifies the fourth element in the array. The colon indicates that we are doing a slice. We have not put a number to the right of the colon, which tells Python to continue on until the end of the array. Specifying a number there would tell it to stop once it reaches that index number. For example ```rows[3:4]``` would return two rows.

At this point we are going to stop and take a minute to prepare the file we will write our data to.

```Python

csvfile = open("movies.csv","wb")

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
    cells = row.find_all('td')
    title = cells[0].text.strip()
    world_box_office = cells[1].text.strip()
    international_box_office = cells[2].text.strip()
    ...
```

There is a lot going on here and we will take it step-by-step, but first a matter of formatting. Once you start a for loop - or any other loop for that matter - Python requires code to be indented in order for it to be included in the loop. Good coding convention says that indent is four spaces (not a tab). Any indented code will be executed as part of that loop, unindented code is outside the loop and will signify its end.

Now the first line of the indented code, ```cells = row.find_all('td')``` is splitting the current row up into another list, this one of the individual cells of that table. This is where we are starting to actually get at our data finally.

A few things going on here. We are assigning each cell to the corresponding variable based on its location or index within the list. The variable ```cells[0]``` refers to the first element in the ```cells``` list by using the [0] notation - remember that Python is zero-based. By placing the numerical index in brackets, we are telling Python to only access the value at that position. 

We are assigning values of the cells to variables named in a way that makes sense to us, so we can easily tell what we are working with.

```Python
    title = cells[0].text.strip()
    world_box_office = cells[1].text.strip()
    international_box_office = cells[2].text.strip()
```

By now you should recognize the notation - we refer to a specific cell by its numerical index enclosed in brackets after the variable name. Next we grab the actual text within the cell by calling ```.text``` on it. Finally we introduce a new step - ```.strip()```. [Strip](http://www.tutorialspoint.com/python/string_strip.htm) removes any excess characters specified within the parentheses from the text. Since we left the parenthese empty, ```strip()``` will remove extra whitespace. This process is executed for each of the three cells which are then assigned to their respective variables. Now it is time to write those cells out to our output file in a csv format.

```Python
    output.writerow([title, world_box_office, international_box_office, domestic_box_office, world_cume, international_cume, domestic_cume, international_distributor, number_territories, domestic_distributor])
 ```

 In order to do this we tell the csv writer that we created that we want it to write a row out to our file. This is done simply with ```output.writerow```. We put the value we want to write out within the parentheses. Now sense this is a csv, the writer will want multiple items it can write out separated by a comma. 

 To do this we create a list of our own within the parentheses - ```[title, world_box_office, international_box_office, domestic_box_office, world_cume, international_cume, domestic_cume, international_distributor, number_territories, domestic_distributor] ```. Lists are enclosed in square brackets and each item is separated by a column. Since the items we want to put into the csv document are stored in variables, we simply list the variable names without any quotation marks. If we wanted to write out actual values, they would be enclosed in quotation marks like ```["Heather","Tom","Chris"]```.

 At this point we have accessed the website, parsed the html, scraped out the data and written it out to a file. The final step is to close the output file to prevent any further changes and free up memory dedicated to keeping it open.

 ```Python
 csvfile.close()
 ```

 This is an important step, you can lose your work by leaving this file open or by opening it again in write mode accidentally. Also notice that this line is not indented at all, it is only carried out after the for loop finishes iterating through all the rows of the html table you are scraping.


#Dealing with JSON from the web
##Scrape many websites and merge them together
_or_
python for converting all your data: json, xml, excel into one big csv!

Let's use an API to get information programmatically.

[Govtrack.us](https://www.govtrack.us/developers/api) has an API. Let's
create a spreadsheet of the 100 latest bills.

Our data comes in a new format: JSON. Show on the whiteboard how it's
basically a combination of data structures we already know about: Lists
and dicts (arrays and objects).

[View the data here](https://s3.amazonaws.com/nicar17/pycar17/bill_track.json)

`get_json_notebook.ipynb` - Use `requests` to get the json data the web

`json_to_csv_notebook.ipynb` - Loop through the parts we care about and create a csv file from the data
