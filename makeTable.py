import csv

class Physician:

	def __init__(self, npi, first_name, last_name, grad_year, school, gender, specialty, zipcode, 
		hospital_ccn, hospital_score):

		self.npi = npi
		self.first_name = first_name
		self.last_name = last_name
		self.grad_year = grad_year
		self.school = school
		self.gender = gender
		self.specialty = specialty
		self.zipcode = [zipcode]
		self.hospital_scores = []
		self.experience = None
		

#TODO in progress

def get_ccn(row):
	if row['Claims based hospital affiliation CCN 1']

[row['Claims based hospital affiliation CCN 1'], hospital_scores[row['Claims based hospital affiliation CCN 1']]],

if __name__ == '__main__':

	mainList = {}
	hospital_scores = {}

	with open('hospital score.csv') as data:
		reader = csv.DictReader(data)
		for row in reader:
			hospital_scores[row['Provider Number']] = row['Total Performance Score']
	data.close()

	with open('National_Downloadable_File.csv') as data:
		reader = csv.DictReader(data)
		counter = 0
		for row in reader:
			if row['NPI'] in mainList:
				mainList[row['NPI']].zipcode.append(row['Zip Code'])
			
			#call a function that checks how many ccn's a physician has, and returns hospital scores.		


			else:
				physician = Physician(row['NPI'], row['First Name'], row['Last Name'], row['Graduation year'], \
				row['Medical school name'], row['Gender'], row['Primary specialty'], row['Zip Code'], \
			



				mainList[physician.npi] = physician
		
			print physician.npi
			counter += 1
			if counter == 10:
				break

	print len(mainList)
	data.close()









	#do something
