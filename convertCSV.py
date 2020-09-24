import csv
import sys

#1. Place each record of a file in a list.
#2. Iterate thru each element of the list and get its length.
#3. If the length is less than one replace with value x.
def replaceNull(filepath):
    rows=[]
    reader = csv.reader(open(filepath, "rt"))
    for row in reader:
        for i, x in enumerate(row):
                    if len(x)< 1:
                            x = row[i] = 0
        rows.append((','.join(str(x) for x in row)).split(','))
        # print(','.join(str(x) for x in row))
    with open('test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)