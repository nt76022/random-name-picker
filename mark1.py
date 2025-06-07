import csv
import random

with open('name2.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)

print(random.choice(data))
#for row in data:
#	print(row)
