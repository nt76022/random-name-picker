import csv
import random
import subprocess

with open('72_demons_names.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)

ran = random.choice(data)
name ="".join(ran)

print(name)

subprocess.run(['wl-copy'], input=name.encode())
