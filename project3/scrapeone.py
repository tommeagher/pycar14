import requests
from bs4 import BeautifulSoup
import csv



r = requests.get('http://www.bls.gov/web/metro/laummtrk.htm')

html = r.text

soup = BeautifulSoup(html)

table = soup.find('table')

rows = table.findAll('tr') 

rows = rows[3:] 

csvfile = open("unemployment.csv","wb")

output = csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

for row in rows:
    cells = row.findAll('td')
    if cells[1].text == "":
        continue
    rank = cells[0].text.strip()
    geography = cells[1].text.strip()
    rate = cells[2].text.strip()
    output.writerow([rank,geography,rate])

csvfile.close()



