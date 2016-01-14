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
        counter = 0
	for row in reader:
          if row['NPI'] in list_of_exclusions:
            row['Exclusions'] = list_of_exclusions[row['NPI']]
            counter += 1
            print row
          else:
            row['Exclusions'] = ''
          #print row
         
          
            

         
         
          writer.writerow([row.get('NPI'), row.get('First Name'), row.get('Last Name'), row.get('School'),
                           row.get('Grad Year'), row.get('Gender'), row.get('Primary Specialty'),
                           row.get('Zip Code'), row.get('Hospital CCN and score'), row.get('Experience'),
                           row.get('Exclusions')])

          
          #print master_list[row['NPI']].get('Exclusions')
          #break
        #print "\n", counter

        
          
          
		
		

