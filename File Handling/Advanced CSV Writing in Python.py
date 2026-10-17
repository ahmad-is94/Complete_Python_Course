import csv
data = [
    ['Product', 'Price', 'Stock'],
    ['Pen', 2.5, 100],
    ['Notebook', 3.0, 50]
]
with open('data.txt', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter='.')
    for row in data:
        writer.writerow(row)
