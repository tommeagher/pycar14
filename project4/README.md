# 3:15 - 4:50 p.m.

## Project #4

Scrape many websites and merge them together
_or_
python for converting all your data: json, xml, excel into one big csv!

Let's use an API to get information programmatically.

[Govtrack.us](https://www.govtrack.us/developers/api) has an API. Let's
create a spreadsheet of the 100 latest bills.

Our data comes in a new format: JSON. Show on the whiteboard how it's
basically a combination of data structures we already know about: Lists
and dicts (arrays and objects).

[View the data here](https://www.govtrack.us/api/v2/bill?congress=114&order_by=-current_status_date)

`step_1.py` - Use `requests` to get the data

`step_2.py` - Loop through the parts we care about

`step_3.py` - Create a csv file from the data

