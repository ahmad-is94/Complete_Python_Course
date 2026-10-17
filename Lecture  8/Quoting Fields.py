import csv

data = [
    ['Name', 'Comment'],
    ['Ali', 'Hello Sir, the work is done"'],
    ['ahmad', 'Great Work']
]

with open('quote.txt','w',newline='') as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    writer.writerows(data)

with open('quote.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    for rows in csvfile:
        print(rows)
import csv

data = [
    ['Name', 'Comment'],
    ['Ali', 'Hello Sir, the work is done"'],
    ['ahmad', 'Great Work']
]

with open('quote.txt','w',newline='') as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

with open('quote.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    for rows in csvfile:
        print(rows)


import csv

data = [
    ['Name', 'Comment'],
    ['Ali', 'Hello Sir, the work is done"'],
    ['ahmad', 'Great Work']
]

with open('quote3.txt','w',newline='') as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

with open('quote.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    for rows in csvfile:
        print(rows)


import csv

data = [
    ['Name', 'Comment'],
    ['Ali', 'Hello Sir, the work is done"'],
    ['ahmad', 'Great Work']
]

with open('quote4.txt','w',newline='') as csvfile:
    writer = csv.writer(csvfile,quoting=csv.QUOTE_NONE)
    writer.writerows(data)

with open('quote.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    for rows in csvfile:
        print(rows)