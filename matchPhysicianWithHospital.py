"""
matchPhysicianWithHospital.py
Author: Rex Chang
11/15/2016

This program takes in the ranked hospital data and matches the hospitals with the physicians. 
Outputs a table with each row being physician NPI, assciated hospital's CCN, hospital score, and ranking.
A physician may be associated with multiple hospitals. 
"""
import csv



output = open('physician_by_hospital_ranking.csv', 'wb')
writer = csv.writer(output)
writer.writerow(["NPI", "[Hospital CCN, [Hospital Score, Ranking]]"])

#creat a dictionary of hospital ccn-score pairs
hospital_list = {}
with open('hospital_sorted_scores.csv') as data:
	reader = csv.DictReader(data)
	for row in reader:
		hospital_list[row['Hospital CCN']] = [row['Hospital Score'], row['Rank']]
data.close()

with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	match = {}
	counter = 0

	for row in reader:
		
		counter += 1
		print counter

		field = row['Hospital CCN and score']
		if field != "[]":
			hospitals_for_one_physician = eval(row['Hospital CCN and score'])
			for i in range(len(hospitals_for_one_physician)):
				hospital_ccn = eval(row['Hospital CCN and score'])[i][0]
				if hospital_ccn in hospital_list.keys():
					if row['NPI'] not in match:
						match[row['NPI']] = [hospital_ccn, hospital_list[hospital_ccn]]
					else:
						match[row['NPI']].append([hospital_ccn, hospital_list[hospital_ccn]])		

data.close()

for key, value in match.items():
	writer.writerow([key, value])
