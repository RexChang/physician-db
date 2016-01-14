import csv



list_of_exclusions = {}

"""
with open('exclusions.csv') as data:
	reader = csv.DictReader(data)
	for row in reader:
		list_of_exclusions[row['npi']] = [row['exclusion_type'], row['exclusion_date']]
		print list_of_exclusions
		list_of_exclusions['KEYYYY'] = "value"
		print list_of_exclusions
		break
	data.close()
"""

with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	for row in reader:
		print row
		break

