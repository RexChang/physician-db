import csv


def total_experience(experience):
        '''returns the total number of procedures a doctor has performed given
        that doctor's "experience" listing in our data'''
        #total = int(experience[1])
        #print experience, "\n\n\n\n\n\n\n\n\n\n\n\n\n"
        temp_str = ''
        i = 0
        j = 0
        while i < len(experience) and j < len(experience):
          if experience[i] == "\'" and experience[i+1] == ',':
            j = i+5
            temp_str = ''
            while experience[j] != "\'":
              temp_str += experience[j]
              j += 1
            i+=j
          else:
            i+=1
        print int(temp_str), "\n"
          #print "\\'", "\n"
            
          #total += int(code[1])
        #return total


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
        
        #Groups NPIs by specialty
        specialty_groups = {}

        physician_scores = {}
	for row in reader:
		if row['NPI'] in list_of_exclusions:
			row['Exclusions'] = list_of_exclusions[row['NPI']]
		else:
			row['Exclusions'] = ''

		specialty_key = row.get('Primary Specialty')
                
		if specialty_key not in specialty_list.keys():
			specialty_list[specialty_key] = 1
                        specialty_groups[specialty_key] = [row.get('NPI'), total_experience(row.get('Experience'))]
		else:
		        specialty_list[specialty_key] += 1
                        specialty_groups[specialty_key].append([row.get('NPI'), total_experience(row.get('Experience'))])
                #print specialty_groups
                #break
                
                
	#print specialty_list
       

          
            

          
          #print master_list[row['NPI']].get('Exclusions')
          #break
        #print "\n", counter

        
          
          
		
		

