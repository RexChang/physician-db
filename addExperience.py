import csv



def total_experience(experience):
        '''returns the total number of procedures a doctor has performed given
        that doctor's "experience" listing in our data'''
        #print experience
        total = 0
        
        if experience == None:
          pass

        else:
          for item in experience:
            proc = int(item[1].strip().replace(",",""))
            total += proc
        return total
    
output1 = open("physician_groupings.csv", 'wb')
writer1 = csv.writer(output1)
writer1.writerow(["Primary Specialty", "Number of Specialists"])


output2 = open("physician_experience.csv", 'wb')
writer2 = csv.writer(output2)
writer2.writerow(["NPI", "First Name", "Last Name", "Procedures Performed"])


with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	specialty_list = {}
        
        #Groups NPIs by specialty
        specialty_groups = {}

        physician_scores = {}
	for row in reader:
                """
		if row['NPI'] in list_of_exclusions:
			row['Exclusions'] = list_of_exclusions[row['NPI']]
		else:
			row['Exclusions'] = ''
                """
		specialty_key = row.get('Primary Specialty')
                
                try:
                  tot_expr = eval(row.get('Experience'))
                except:
                  tot_expr = None
                
		if specialty_key not in specialty_list.keys():
			specialty_list[specialty_key] = 1
                        
                        #specialty_groups[specialty_key] = [row.get('NPI'), total_experience(tot_expr)]
                        specialty_groups[row.get('NPI')] = [total_experience(tot_expr), row.get('First Name'), row.get('Last Name')]
		else:
		        specialty_list[specialty_key] += 1
                        #specialty_groups[specialty_key].append([row.get('NPI'), total_experience(tot_expr)])
                        specialty_groups[row.get('NPI')] = [total_experience(tot_expr), row.get('First Name'), row.get('Last Name')]
                #print specialty_groups
data.close()

#Export a csv containing a list of specialties, and the number of doctors in each specialty
for key, value in specialty_list.items():
    writer1.writerow([key, value])
            
output1.close

#Export a csv containing a list of doctors (NPI, Name) & the total number of procedures performed by each doctor
# (0 if not available)
for key, value in specialty_groups.items():
    writer2.writerow([key, value[1], value[2], value[0]])

output2.close
