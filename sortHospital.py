import csv



output = open('hospital_sorted_scores.csv', 'wb')
writer = csv.writer(output)
writer.writerow(["Hospital CCN", "Hospital Score", "Rank"])

with open('physician_data.csv') as data:
	reader = csv.DictReader(data)
	hospital_list = []
	counter = 0

	for row in reader:
		
		counter += 1
		print counter

		#create a list of [hospital ccn, hospital score]
		hospital_CCN_and_score = eval(row['Hospital CCN and score'])
		
		for entry in hospital_CCN_and_score:
			if entry not in hospital_list:
				hospital_list.append(entry)

	#sort list based on hospital score		
	hospital_list.sort(key=lambda x:x[1])
	for i in range(len(hospital_list)):
		hospital_list[i].append(len(hospital_list)-i)
		writer.writerow(hospital_list[i])

