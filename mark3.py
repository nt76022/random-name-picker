import csv
import random
import subprocess
import streamlit as st

st.title("mark3")

if st.button("gen"):

	with open('namehalf.csv', newline='') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)



	ran = random.choice(data)
	name ="".join(ran)

	st.write(name)

	subprocess.run(['wl-copy'], input=name.encode())
