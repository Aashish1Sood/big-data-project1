import csv

#writing into the final merged output file
tsvout=open('../ufo_airport_meteorite_scifi_merged.tsv', 'w')


#reading data from the merged file of the meteor data and the sci_fi dataset created
with open('../ufo_airport_meteorite.tsv','rb') as tsvin,open('sci_fi_output.tsv','rb') as sci_fi_input:
    sci_fi_input = csv.reader(sci_fi_input, delimiter='\t')
    tsvin = csv.reader(tsvin, delimiter='\t')

    #adding the sci_fi data into a dictionary of years 
    sci_fi_dict = {}
    for i,row in enumerate(sci_fi_input):
    	if i==0:
    		continue
    	year = row[0]
    	sci_fi_dict[year]=[row[1],row[2],row[3],row[4]]


    #joining of data of scifi movies and ufo sightings
    for i,row in enumerate(tsvin):
    	if i==0:
    		for col in row:
    			tsvout.write(col+'\t')
    		tsvout.write("Number of sci_fi movies released\tNumber of ufo sightings\tRatio of number of ufo sightings to number of movies released in that year \tPossibility of ufo_sighting being a dillusion after a sci-fi movie being released?\n")
    	else:
    		year = row[0][0:4]
    		if year not in sci_fi_dict:
				year = row[1][0:4]
    		for col in row:
    			tsvout.write(col+'\t')

    		if year in sci_fi_dict:
    			tsvout.write(sci_fi_dict[year][0]+'\t'+sci_fi_dict[year][1]+'\t'+sci_fi_dict[year][2]+'\t'+sci_fi_dict[year][3]+'\n')
    		else:
    			tsvout.write('\n')
