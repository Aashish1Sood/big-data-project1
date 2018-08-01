#This code is to correct the longitude and latitude values of the US cities which share names with cities in Mexico and Canada
#For the cities where the distance of nearestairport was found to be more than 1000 miles, the lat and long were re queried by appending the locationstring
#with State name, USA. Now these new Longitude and latitude were compared. If the difference in eany one is more than six degrees, the long and lat values were corrected
#and nearest distance is recomputed and updated in DB
import csv
from time import sleep
from collections import defaultdict
from geopy.distance import vincenty
import pickle

from pymongo import MongoClient

airport_fname = "airport_data.pickle"
us_neighbor_fname = "neighbour_dict.pickle"

with open(airport_fname, 'rb') as f:
    airport_data = pickle.load(f)
with open(us_neighbor_fname, 'rb') as f:
    us_neighbour_data = pickle.load(f)

def generateAirportList(region_list):
    airport_list = []
    for region in region_list:
        airport_list = airport_list + airport_data[region]
    return airport_list

def findNearest(city,region_list):
    airport_list = generateAirportList(region_list)
    city_lat_lon = (float(city['latitude']),float(city['longitude']))
    min_dist = None
    airport_name = None
    for airport in airport_list:
        airport_lat_lon = (airport[1],airport[2])
        vin_dist = vincenty(city_lat_lon, airport_lat_lon).miles
        if min_dist is None:
            min_dist = vin_dist
            airport_name = airport[0]
        else:
            if vin_dist < min_dist:
                min_dist = vin_dist
                airport_name= airport[0]
    return airport_name,min_dist

def checkDiff(a,b):
    if abs(a[0] - b[0]) >=6 and abs(a[1] - b[1]) >=6:
        return True
    else:
        return False

db = MongoClient().ufo.cities
with open("new_us_lon_lat.pickle", 'rb') as f1:
    us_dict = pickle.load(f1)
count = 0
tcount=0

for row in db.find():
    region = row['region']
    if row['Distance'] >1000:
        tcount+=1
        location = row['location'].strip()
        print(location)
        loc = (row['latitude'],row['longitude'])
        if location in us_dict and checkDiff(us_dict[location],loc):
            count+=1
            print(location,loc,us_dict[location])
            row['latitude'] = us_dict[location][0]
            row['longitude'] = us_dict[location][1]
            if region[:3] == "US-":
                region_list = us_neighbour_data[region][:]
                region_list.append(region)
                airport_name, dist = findNearest(row, region_list)
                print("New Dist:- ",dist)
                db.update_one({'_id': row['_id']}, {"$set": {'latitude':us_dict[location][0],'longitude':us_dict[location][1],'Nearest Airport': airport_name, 'Distance': dist}})

print(count,tcount)