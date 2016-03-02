## Mission: extract steps necessary for rubber duck debugging from the website and print them one per line on your screen
## some places have a commented 'print' statement. Uncomment them when needed (by removing the #) to see the result.

import requests, unicodecsv
from bs4 import BeautifulSoup as bs

website = "http://homolova.sk/Rubber Duck Debugging.html
r = requests.get(website)
soup = bs(r.text) # .text is a method that extract the text. In requests it's the HTML structure. In BeautifulSoup the text without tags.
#print soup

steps = soup.find_all("p")
#print steps

steps_list = []
#print steps_list
steps_list.append(steps[1].text)
#print steps_list
steps_list.append(steps[2].text)
#print steps_list
steps_list.append(steps[3].text
#print steps_list
steps_list.append(setps[4].text)
#print steps_list

for step in steps_list
    print setp