import csv

class Physician:

	def __init__(self, npi, first_name, last_name, grad_year, school, gender, specialty, zipcode, 
		hospital_scores):

		self.npi = npi
		self.first_name = first_name
		self.last_name = last_name
		self.grad_year = grad_year
		self.school = school
		self.gender = gender
		self.specialty = specialty
		self.zipcode = [zipcode]
		self.hospital_scores = hospital_scores
		self.experience = None
		

"""
get_scores: matches a physician's ccn with the hospital database. returns a list of hospital ccn's and its respective score for a physician.
Input: row(a row in the physician database, represents a physician), hospital_scores(a dictionary of hospital ccns and their scores)
"""
def get_scores(row, hospital_scores):
	list_of_ccn = []
	if row['Claims based hospital affiliation CCN 1'] != '':
		try:
			list_of_ccn.append([row['Claims based hospital affiliation CCN 1'], hospital_scores[row['Claims based hospital affiliation CCN 1']]])
		except KeyError:
			pass
	else:
		return list_of_ccn

	if row['Claims based hospital affiliation CCN 2'] != '':
		try:
			list_of_ccn.append([row['Claims based hospital affiliation CCN 2'], hospital_scores[row['Claims based hospital affiliation CCN 2']]])
		except KeyError:
			pass
	else:
		return list_of_ccn

	if row['Claims based hospital affiliation CCN 3'] != '':
		try:
			list_of_ccn.append([row['Claims based hospital affiliation CCN 3'], hospital_scores[row['Claims based hospital affiliation CCN 3']]])
		except KeyError:
			pass
	else:
		return list_of_ccn

	if row['Claims based hospital affiliation CCN 4'] != '':
		try:
			list_of_ccn.append([row['Claims based hospital affiliation CCN 4'], hospital_scores[row['Claims based hospital affiliation CCN 4']]])
		except KeyError:
			pass
	else:
		return list_of_ccn

	return list_of_ccn

if __name__ == '__main__':

	mainList = {}
	hospital_scores = {}

	# create a dictionary of hospital ccn and score pairs
	with open('hospital scores.csv') as data:
		reader = csv.DictReader(data)
		for row in reader:
			hospital_scores[row['Provider Number']] = row['Total Performance Score']
	data.close()

	# create a dictionary of physician npi and physician object pairs
	with open('National_Downloadable_File.csv') as data:
		reader = csv.DictReader(data)
		counter = 0
		for row in reader:
			if row['NPI'] in mainList:
				mainList[row['NPI']].zipcode.append(row['Zip Code'])

			else:
				list_of_ccn = get_scores(row, hospital_scores)
				physician = Physician(row['NPI'], row['First Name'], row['Last Name'], row['Graduation year'], \
				row['Medical school name'], row['Gender'], row['Primary specialty'], row['Zip Code'], list_of_ccn)

				mainList[physician.npi] = physician
		
			#print physician.npi
			counter += 1
			if counter == 500:
				break
	data.close()


	# write out data
	with open('physician_data.csv', 'wb') as output:
		writer = csv.writer(output) 
		writer.writerow(["NPI", "First Name", "Last Name", "School", "Grad Year", "Gender", 
			"Primary Specialty", "Zip Code", "Hospital CCN and score", "Experience"])
		for key, value in mainList.items():
			writer.writerow([key, value.first_name, value.last_name, value.school, value.grad_year, 
				value.gender, value.specialty, value.zipcode, value.hospital_scores, value.experience])

	output.close()			





	#do something
