"""
makeTable.py
1/11/2016
Authors: Rex Chang, Maddox Riley

This program gathers several databases and merges all relevant data into the main physician database.
The output file is physician_data.csv, where each row contains information about a physician. 
note: need to make sure the csv files name match
"""

import csv

"""
This Physician object contains the relevant fields that we want to store in the database. Can always
add more or edit.
"""
class Physician:

	def __init__(self, npi, first_name, last_name, grad_year, school, gender, specialty, zipcode, 
		hospital_scores, experience):

		self.npi = npi
		self.first_name = first_name
		self.last_name = last_name
		self.grad_year = grad_year
		self.school = school
		self.gender = gender
		self.specialty = specialty
		self.zipcode = [zipcode]
		self.hospital_scores = hospital_scores
		self.experience = experience
		

"""
get_scores: matches a physician's ccn with the hospital database. returns a list of hospital ccn's and its respective score for a physician.
Input: row(a row in the physician database, represents a physician), hospital_scores(a dictionary of hospital ccns and their scores). There
are at most 4 hospitals for a physician.
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


def get_experience(filename, procedures):
        '''reads in a single CSV file containing data about procedures performend
        by physicians. Appends data as appropriate based on NPIs'''

        with open(filename) as data:
                data.next()
                reader = csv.DictReader(data)
                index = 0
                for row in reader:
                  #for each physician, key is the NPI & value is a list of [HCPCS code, num  procedures]    
                  entry = [row['hcpcs_code'], row[' line_srvc_cnt ']]

                  #there may be multiple rows per physician. check for this case
                  if row['npi'] not in procedures: 
                    procedures[row['npi']] = [entry]
                  else:
                    procedures[row['npi']].append(entry)

        data.close()


if __name__ == '__main__':

	mainList = {}
	hospital_scores = {}
	procedures = {}

	# create a dictionary of hospital ccn and score pairs
	# this is the hospital data
	with open('hospital scores.csv') as data:
		reader = csv.DictReader(data)
		for row in reader:
			hospital_scores[row['Provider Number']] = row['Total Performance Score']
	data.close()

	#these are the procedure data sorted by physician last name
	experience_filenames = ["2013_Procedures/2013_Procedures_A.csv", "2013_Procedures/2013_Procedures_B.csv",
     "2013_Procedures/2013_Procedures_C.csv",  "2013_Procedures/2013_Procedures_D.csv", 
     "2013_Procedures/2013_Procedures_EFG.csv",  "2013_Procedures/2013_Procedures_HIJ.csv", 
     "2013_Procedures/2013_Procedures_KL.csv",  "2013_Procedures/2013_Procedures_MN.csv", 
     "2013_Procedures/2013_Procedures_OPQ.csv",  "2013_Procedures/2013_Procedures_R.csv", 
     "2013_Procedures/2013_Procedures_S.csv",  "2013_Procedures/2013_Procedures_TUVWX.csv", 
     "2013_Procedures/2013_Procedures_YZ.csv"]

	for name in experience_filenames:
		get_experience(name, procedures)

	# create a dictionary of physician npi and physician object pairs
	# this is the physician database
	with open('National_Downloadable_File.csv') as data:
		reader = csv.DictReader(data)
		for row in reader:
			#there will only be multiple rows of the same NPI if the physician has multiple zip codes
			if row['NPI'] in mainList:
				mainList[row['NPI']].zipcode.append(row['Zip Code'])

			else:
				list_of_ccn = get_scores(row, hospital_scores)

				# set fields for the Physician object
				physician = Physician(row['NPI'], row['First Name'], row['Last Name'], row['Graduation year'], \
				row['Medical school name'], row['Gender'], row['Primary specialty'], row['Zip Code'], list_of_ccn, None)

				mainList[physician.npi] = physician

				try:
					physician.experience = procedures[row['NPI']]
				except KeyError:
					pass
		
	data.close()

	# write out data
	with open('physician_data.csv', 'wb') as output:
		writer = csv.writer(output) 
		#write out column names
		writer.writerow(["NPI", "First Name", "Last Name", "School", "Grad Year", "Gender", 
			"Primary Specialty", "Zip Code", "Hospital CCN and score", "Experience"])
		for key, value in mainList.items():
			writer.writerow([key, value.first_name, value.last_name, value.school, value.grad_year, 
				value.gender, value.specialty, value.zipcode, value.hospital_scores, value.experience])

	output.close()			