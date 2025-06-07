import csv
import random
import subprocess

# Ask the user for gender
gender_choice = input("What gender do you want? (boy/girl/random): ").strip().lower()

while gender_choice not in ['boy', 'girl', 'random']:
    print("Invalid choice. Try again.")
    gender_choice = input("What gender do you want? (boy/girl/random): ").strip().lower()

# Read CSV and filter
data = []
with open('name.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # This is the fix!
    for row in reader:
        if gender_choice == 'random' or row['gender'].lower() == gender_choice:
            data.append(row['name'])

# Pick and show name
if data:
    name = random.choice(data)
    print(f"Random Name: {name}")
    subprocess.run(['wl-copy'], input=name.encode())  # Copy to clipboard
else:
    print("No names found for that gender.")

