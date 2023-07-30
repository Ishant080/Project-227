import json

data_from_csv = []

with open('data_set.txt', 'r') as f:
	data_from_txt = json.loads(f.read())

csvfilestore = open('Enter_csv_file_name', 'w', newline='')

with open('data_set.txt', 'r') as file:
	reader = csv.reader(file)