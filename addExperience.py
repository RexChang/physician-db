"""
This script merges the initial conglomorated output with data about how many procedures each physician has performed.


"""

import csv
import operator



def total_experience(experience):
        '''returns the total number of procedures a doctor has performed given
        that doctor's "experience" listing in our data
        Since each doctor performs multiple procedures, the goal is to return a *total* number of procedures of all kinds
        '''
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

"""
output2 = open("physician_experience.csv", 'wb')
writer2 = csv.writer(output2)
writer2.writerow(["NPI", "First Name", "Last Name", "Primary Specialty", "Procedures Performed"])
"""

#Open main collection of data on physicians
with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	specialty_list = {}
        
        #Groups NPIs by specialty
        specialty_groups = {}

        physician_scores = {}

        scores_sort = []
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
                #Build a dictionary of specialties where the value is a list of [NPI, # Procedures performed]
		if specialty_key not in specialty_list.keys():
			specialty_list[specialty_key] = [[row.get('NPI'), total_experience(tot_expr)]]
                        
                        #specialty_groups[row.get('NPI')] = [total_experience(tot_expr), row.get('First Name'), row.get('Last Name'), \
                        #                                    row.get('Primary Specialty')]
		else:
                        specialty_list[specialty_key].append([[row.get('NPI'), total_experience(tot_expr)]])
                        #specialty_groups[row.get('NPI')] = [total_experience(tot_expr), row.get('First Name'), row.get('Last Name'), \
                        #                                    row.get('Primary Specialty')]
                #print specialty_groups
data.close()


for key, value in specialty_list.items():
    
    #Within each specialty, sort doctors by # of procedures performed
    #We could insert a search function to show a ranking

    #Doesn't seem to work for some reason (?) -> list index out of range
    value.sort(key=lambda x: x[1])

    #Export a csv containing a list of specialties, and the number of doctors in each specialty
    writer1.writerow([key, len(value)])
    
            
output1.close

"""
#Export a csv containing a list of doctors (NPI, Name) & the total number of procedures performed by each doctor
# (0 if not available)
for key, value in specialty_groups.items():
    writer2.writerow([key, value[1], value[2], value[3], value[0]])

output2.close
"""

