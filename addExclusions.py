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
with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	specialty_list = {}
	for row in reader:
		if row['NPI'] in list_of_exclusions:
			row['Exclusions'] = list_of_exclusions[row['NPI']]
		else:
			row['Exclusions'] = ''

			specialty_key = row.get('Primary Specialty')
			if specialty_key not in specialty_list.keys():
				specialty_list[specialty_key] = 1
			else:
				specialty_list[specialty_key] += 1

	print specialty_list

          
            

          
          #print master_list[row['NPI']].get('Exclusions')
          #break
        #print "\n", counter

        
          
          
		
		

