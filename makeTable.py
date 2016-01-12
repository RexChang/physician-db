import csv


class Physician:

	def __init__(self, npi, first_name, last_name, grad_year, school, gender, specialty, zipcode, 
		hospital_ccn, hospital_score, hcpcs, procedures):
		self.npi = npi
		self.first_name = first_name
		self.last_name = last_name
		self.grad_year = grad_year
		self.school = school
		self.gender = gender
		self.specialty = specialty
		self.zipcode = [zipcode]
		self.hospital_ccn = hospital_ccn
		self.hospital_score = hospital_score
		self.hcpcs = hcpcs
		self.procedures = procedures
if __name__ == '__main__':

	mainList = {}

	hospital_score = 0
	hcpcs = 0
	procedures = 0


	with open('National_Downloadable_File.csv') as data:
		reader = csv.DictReader(data)
		counter = 0
		for row in reader:

			if row['NPI'] in mainList:
				mainList[row['NPI']].zipcode.append(row['Zip Code'])
			
			else:
				physician = Physician(row['NPI'], row['First Name'], row['Last Name'], row['Graduation year'], 
					row['Medical school name'], row['Gender'], row['Primary specialty'], row['Zip Code'], 
					row['Claims based hospital affiliation CCN 1'], hospital_score, hcpcs, procedures)
			
				mainList[physician.npi] = physician
		
			print physician.npi
			counter += 1
			if counter == 10:
				break

	print len(mainList)




	#do something
