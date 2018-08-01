import json
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut

import csv
from time import sleep
from collections import defaultdict
from geopy.distance import vincenty
import pickle

with open('ufo_awesome.json',encoding="utf8") as json_data:
    ufo_data = json.load(json_data)
    print(len(ufo_data))
    print(ufo_data[0])

us_state_code = open('state_code.csv', "r")
us_state = csv.reader(us_state_code)
state_set = set() #set containing the 2 letter state codes in US
for row in us_state:
    state_code = row[0].split(",")[1].replace("\"","").upper()
    state_set.add(state_code)
print(state_set)
count = 0

# US sightings
# There is a list of neighbouring USA states.
# from this we can form the region ISO code. this will help narrow down the search of airports.
# There are 9019 non US sightings.
# reverse query will help get the country and state of the sighting.
# all the airports in the list have their corresponding region ISO code.
# From the country and state we got from the reverse query, we need to form the region ISO code.
# Need to find a way to generate region ISO code from state and country. GeoName package can help. but need to search more on this.
ufo_region_data=[]
count=0
exception = False
geocod_dict = {}

for i,data in enumerate(ufo_data):
    exception = False
    if i%10 == 0:
        print(i) # print count for every 10th iteration
    if i%300 == 0:
        if i != 0:
            print("Create a new file")
            fname = "ufo_region_data"+str(count)+".pickle"
            count = count+1
            #Create pickle files for every 300 locationsinthe original UFO sighting JSON
            with open(fname, 'wb') as f:
                pickle.dump(ufo_region_data, f)
                ufo_region_data = []
    d={}
    location = data["location"]
    try:
        if location not in geocod_dict:
            geo_location = geolocator.geocode(location,timeout=10)  # Get the geocode values from the API
            geocod_dict[location] = geo_location
        else:
            geo_location = geocod_dict[location]
    except GeocoderTimedOut as e:
        print(location,i)
        exception = True
    if geo_location is not None and exception == False:
        d['lat'],d['lon'] = geo_location.latitude, geo_location.longitude
        split_loc = location.split(",")
        if split_loc[-1].strip().upper() not in state_set: # This check is for Non US states, we need to capture the country/region using the reverse query.
            query_string = str(geo_location.latitude)+", "+str(geo_location.longitude)
            try:
                reverse_loc = geolocator.reverse(query_string,timeout=10)
                if 'address' in reverse_loc.raw and 'country_code' in reverse_loc.raw['address']:
                    d["country"] = reverse_loc.raw['address']['country_code'].upper()
                    d["region"] = d["country"]
            except GeocoderTimedOut as e:
                print("Timeout in reverse query")
                print(location, i)
        else:
            d["country"] = "US"
            d["state"] = split_loc[-1].strip().upper()
            d["region"] = d["country"]+"-"+d["state"]
    ufo_region_data.append(d)
    sleep(1) # Introduced sleep parameter to notoverwhelm thethe geopy API with too many requests


