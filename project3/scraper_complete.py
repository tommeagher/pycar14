#Import our modules or packages that we will need to scrape a website
import requests
from bs4 import BeautifulSoup
import csv


#Make a request to the webpage url that we are scraping
r = requests.get('http://www.bls.gov/web/metro/laummtrk.htm')

#Assign the html code from that site to a variable
html = r.text

#parse the html
soup = BeautifulSoup(html)

#isolate the table
table = soup.find('table')

#find the rows
rows = table.findAll('tr') 

#oops have some bad rows, let's get rid of them
rows = rows[3:] 

#open our output file
csvfile = open("unemployment.csv","wb")

#point our csv.writer at the output file and specify the necessary parameters
output = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

#loop through the rows
for row in rows:
    #grab the table cells from each row
    cells = row.findAll('td')
    #skip the blank rows
    if cells[1].text == "":
        continue
    #assign the cell values to variables
    rank = cells[0].text.strip()
    geography = cells[1].text.strip()
    rate = cells[2].text.strip()
    #write the variables out to a csv file
    output.writerow([rank,geography,rate])

#close the csv file
csvfile.close()

#win