#Import our modules or packages that we will need to scrape a website
import requests
from bs4 import BeautifulSoup
import csv


#Make a request to the webpage url that we are scraping
r = requests.get('https://s3-us-west-2.amazonaws.com/nicar-2015/Weekly+Rankings+-+Weekend+Box+Office+Results+++Rentrak.html')

#Assign the html code from that site to a variable
html = r.text

#parse the html
soup = BeautifulSoup(html)

#isolate the table
table = soup.find('table',{'class':'entChartTable'})

#find the rows, at the same time we are going to use slicing to skip the first two header rows.
rows = table.findAll('tr')

rows = rows[2:]

#open our output file
csvfile = open("movies.csv","wb")

#point our csv.writer at the output file and specify the necessary parameters
output = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

#loop through the rows
for row in rows:
    #grab the table cells from each row
    cells = row.findAll('td')
    #skip the blank rows
    #assign the cell values to variables
    title = cells[0].text.strip()
    world_box_office = cells[1].text.strip()
    international_box_office = cells[2].text.strip()
    domestic_box_office = cells[3].text.strip()
    world_cume = cells[4].text.strip()
    international_cume = cells[5].text.strip()
    domestic_cume = cells[6].text.strip()
    international_distributor = cells[7].text.strip()
    number_territories = cells[8].text.strip()
    domestic_distributor = cells[9].text.strip()

    #write the variables out to a csv file
    output.writerow([title, world_box_office, international_box_office, domestic_box_office, world_cume, international_cume, domestic_cume, international_distributor, number_territories, domestic_distributor])

#close the csv file
csvfile.close()

#win
