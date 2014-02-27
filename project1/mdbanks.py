#import your csv module
import csv

file_name = 'fdic_failed_bank_list.csv'

#open the file to read and create the reader object
csv_file = open(file_name,'rb')
csv_data = csv.reader(csv_file)

#open the file to write and create the writer object
output_file = open('md_banks.csv', 'wb')
writer = csv.writer(output_file, delimiter=',')

#write our header row to the output csv
header_row = csv_data.next()

writer.writerow(header_row)

#loop through and just write the banks in Maryland to the output file
for row in csv_data:
    if row[2] == 'MD':
        writer.writerow(row)
    else:
       continue

csv_file.close()
output_file.close()