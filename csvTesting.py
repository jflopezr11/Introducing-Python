import csv

f = open('TSLA.csv')
reader = csv.DictReader(f)

for country in reader: 
    print(country['country'])
