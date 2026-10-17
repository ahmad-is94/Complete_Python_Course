# import csv
#
# # List of dictionaries representing rows
# data = [
#     {'Name': 'John', 'Age': 20, 'City': 'Hyderabad'},
#     {'Name': 'Sachin', 'Age': 21, 'City': 'Pune'},
#     {'Name': 'Lucy', 'Age': 40, 'City': 'New York'}
# ]
#
# # Writing to CSV using DictWriter
# with open('demo.csv', 'w', newline='') as file:
#     fieldnames = ['Name', 'Age', 'City']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()  # Write header row
#     writer.writerows(data)
import csv

rows = [
    ['Name', 'Age', 'City'],
    ['Rohan', 22, 'New Delhi'],
    ['Abhay', 23, 'Noida'],
    ['Vivek', 24, 'Gurgaon']
]
with open ('list.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

with open ('list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
