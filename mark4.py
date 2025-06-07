import csv
import random
import subprocess

gender_choice = input("what gender do you want? (boy/girl/random): ").strip().lower()

while gender_choice not in ['boy', 'girl', 'random']:
	print("do again")
	gender_choice = input("what gender do you want? (boy/girl/random): ").strip().lower()

data = []
with open('name.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
#	data = list(reader)
#print("what gender do you want"	)
		if gender_choice == 'random' or row['gender'].lower() == gender_choice:
			data.append(row['name'])

if data:			
	name = random.choice(data)
	print(f"Random Name: {name}")
	subprocess.run(['wl-copy'], input=name.encode())
else:
	print("no name found")
