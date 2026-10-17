import csv
with open('E:\\Python_Course\\demo.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
import csv

with open('E:\\Python_Course\\demo.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
         print(row)


import pandas as pd
df = pd.read_csv("E:\\Python_Course\\demo.csv")
print(df)

