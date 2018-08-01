#Analysis of UFO Sightings Data
There are 5 major sub-folders in this repository. 
One for each of the 3 datasets, one for the airport and one for tika-similarity computation for all the joined features of 4 datasets.
Each folder for dataset contains the python scripts to extract the features, the input data required to process the data and its resulting output. The tika_similarity folder contains python scripts for computing EditDistance similarity, cosine similarity and jaccard similarity for the features present in joined dataset.

The main input file containing the ufo data is :- ufo_awesome.json
The intermediate files are as following:-
1) UFO sighting dataset with airport and meteorite :- ufo_airport_meteorite.TSV
2) UFO sighting dataset with airport and meteorite and scifi Movies dataset :- ufo_airport_meteorite_scifi_merged.TSV

The main modified output file containing the ufo data is :- ufo_awesome_FINAL_OUTPUT.tsv

The libraries used/need to be installed are:-
pip3 install json
pip3 install geopy
pip3 install csv
pip3 install pickle
pip3 install pymongo
pip3 install pandas
pip install BeautifulSoup
pip install bs4
pip install urlib2
pip install tika
pip install editdistance
Also make sure mongo is running on the terminal

The important files present in the folders are :-

##1) geo.py
-- Used to read the ufo_awesome.json file and geocode it to find the latitude and longitude of all the locations in the ufo_sightings.
-- Made use of pickle to store the geocoded data into chunks of 300 as the geopy api has a constraint of geocoding only a limited number of locations per API after which the program gives a timeout error.
-- For locations in countries outside the US, we have reverse geocoded them to get their respective regions


##2) combine_pickle_files.py
-- Used to combine the chunks of pickle files into a single pickle file


3) merge_and_cache.py
-- Used to merge the location and coordinates of the ufo_sightings and cache them using mongodb


4) NearDist.py
-- Used to find the nearest airport to a geocoded location. We are storing all the unique locations in the Mongo DB
-- For US locations, we find nearest airport by assuming that it would be in either same state or in theneighbouring state. For US neighbouring state we are using the pickle file neighbour_dict.pickle
-- For non-US locations, we assume that the nearest airport will be in the same country.


5) wiki_scifi.py
-- Used to scrape the Wikipedia page containing all the sci-fi movie lists released till date and stores it in a file named sci-fi_database.csv


6) sci_fi.py
-- Used to combine the sci-fi_database.csv and the ufo_awesome sightings to produce the resultant sci_fi_output.tsv file with its 3 features.


7) meteor.py
-- Use Meteorite_Landings.csv as the dataset. Index it based upon the year of the meteor landing.
-- Merge the unique locations stored in mongoDB to the UFO sighting Dataset.
-- Find the nearest meteor landings based on geocoded locations and the year.


8)getYearWiseUFOCount.py
-- Used to just understand the no.of UFO sightings recorded or sighted in each year. 
-- This helped us to focus on the census data for the years where the highest sightings are reported (>400 ~ around 0.6 percentile of the total sightings) 


9)UFO_Join_Census.py
-- joins UFO data with Census data (of 2000,2010) which covers timeperiod from 1991 to 2010. 
-- We group and count the UFO sightings by County and join this with the Census data
-- Output no.of sightings in a state, county and the year with the respective population density and housing density.


10) USNeighbours.py
-- Used to find all the neighbouring states of each state to help calculate the nearest airport. Output is stored in a pickle.


11)lat_long_correction.py
-- This code is used to correct some of the lat_long errors occured during geocoding due to the wrong state being considered for some cities, where these city names are present in more than one state.	


12) merging_scifi_ufo.py
-- This code is used to merge and join the ufo sighting data with the sci-fi data created.


13) pickleDumpDict.py
-- This code is used to extract data from the joined data from all the datasets in ufo_awesome_FINAL_OUTPUT.tsv, create the dictionary of the features and a list of their corresponding values.


14) editDist.py
-- Used to compute edit distance similarity metric for the features in the joined dataset. 


15) cosine_similarity.py
-- Used to compute cosine similarity metric for the features in the joined dataset. 


16) jaccard_similarity.py
-- Used to compute jaccard similarity metric for the features in the joined dataset. 


17) create-cluster.py
-- Reads in the the similarity.csv files and create clusters in clusters.json based on x-coordinate.


18) cluster-d3.html
-- Reads in cluster.json and renders the clusters in the html format.


19)AggregateRuralData.py
-- Sums up all UFO sightings in rural areas per year. Using this output we calculate percentage of UFO sightings in rural areas.


20)mergeAirportData.py
-- This script merges the UFO sighting data with the Airport data.


21)ConvertPickleToTSV.py
-- This script converts pickle file,json to TSV file.


22)airports.py
-- This script will read the airports.csv dataset and will create a pickle file for the same.




The order in which the programs need to be executed:
1. geo.py
2. combine_pickle_files.py
3. merge_and_cache.py
4. USNeighbours.py
5. airports.py
6. NearDist.py
7. lat_long_correction.py
8. mergeAirportData.py
9. meteor.py
10. ConvertPickleToTSV.py
11. wiki_scifi.py
12. sci_fi.py
13. merging_scifi_ufo.py
14. getYearWiseUFOCount.py
15. UFO_Join_Census.py
16. AggregateRuralData.py
17. pickleDumpDict.py
18. editDist.py
19. cosine_similarity.py
20. jaccard_similarity.py
21. create-cluster.py
22. cluster-d3.py

