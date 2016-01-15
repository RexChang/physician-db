import csv



list_of_exclusions = {}


with open('exclusions.csv') as data:
	reader = csv.DictReader(data)
	for row in reader:
		list_of_exclusions[row['npi']] = [row['exclusion_type'], row['exclusion_date']]
	data.close()

output = open('new_physician_data.csv', 'wb')
writer = csv.writer(output)
writer.writerow(["NPI", "First Name", "Last Name", "School", "Grad Year", "Gender", 
			   "Primary Specialty", "Zip Code", "Hospital CCN and score", "Experience", "Exclusions"])

hospital_output = open


with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	specialty_list = {}
	hospital_list = []

	counter = 0
	for row in reader:
		if row['NPI'] in list_of_exclusions:
			row['Exclusions'] = list_of_exclusions[row['NPI']]
		else:
			row['Exclusions'] = ''

		"""	
		#create a dictionary of specialty-count for the entire db	
		specialty_key = row.get('Primary Specialty')
		if specialty_key not in specialty_list.keys():
			specialty_list[specialty_key] = 1
		else:
			specialty_list[specialty_key] += 1
		"""
			
		#create a list of [hospital ccn, hospital score]
		hospital_CCN_and_score = eval(row['Hospital CCN and score'])
		for entry in hospital_CCN_and_score:
			if entry not in hospital_list:
				hospital_list.append(entry)
	
	#sort list based on hospital score		
	hospital_list.sort(key=lambda x:x[1])
	print hospital_list

	#print specialty_list
        
    #TODO: get the write to new output part
            
          
          
		
		

