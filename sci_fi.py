import csv
import json

sci_fi_database_reader = open('sci-fi_database.csv', 'r')
sci_fi = csv.reader(sci_fi_database_reader)

with open('ufo_awesome.json') as json_data:
    ufo_data = json.load(json_data)


#combines the data from the sci-fi databased created the ufo_sightings dataset to get the 3 features - the Year the movie was released and the sighting took place, 
#the ratio of the number of sightings to the number of movies released and the if it could be possible that due to watching a sci-fi movie, the sighter confused an aircraft to be a ufo
sci_fi_output = open('sci_fi_output.tsv','w')

sci_fi_dict = {}
for row in sci_fi:
	year=row[0]
	if year.isdigit():
		if year in sci_fi_dict:
			sci_fi_dict[year]=sci_fi_dict[year]+1
		else:
			sci_fi_dict[year]=1

ufo_dict = {}
for row in ufo_data:
	year = row['sighted_at'][0:4]
	if year ==0:
		year = int(row['reported_at'][0:4])
	if year in ufo_dict:
		ufo_dict[year] = ufo_dict[year]+1
	else:
		ufo_dict[year]= 1
yes_counter=0
no_counter=0
sci_fi_output.write("year\tNumber of sci_fi movies released\tNumber of ufo sightings\tratio of number of movies released to number of sightings that took place in that year \tPossibility of ufo_sighting being a dillusion after a sci-fi movie being released?\n")
for year in sci_fi_dict:
	if year in ufo_dict:
		if(ufo_dict[year]/sci_fi_dict[year]<2): #checking if the ratio is less than 2 where it is considered to be a possibility`
			possible = "Yes"
			yes_counter = yes_counter+1
		else:
			possible = "No"
			no_counter = no_counter+1
		ratio = float(ufo_dict[year])/float(sci_fi_dict[year])
		sci_fi_output.write(str(year)+'\t'+str(sci_fi_dict[year])+'\t'+str(ufo_dict[year])+'\t'+str(ratio)+'\t'+possible+'\n')

print "Number of possible true dillusions "+str(yes_counter)
print "Number of possible false dillusions "+str(no_counter)
total_counter = yes_counter+no_counter
percent_of_yes = float(yes_counter)/total_counter*100
percent_of_no = float(no_counter)/total_counter*100
print "Percent of possible true dillusions "+str(percent_of_yes)
print "Percent of possible false dillusions "+str(percent_of_no)


