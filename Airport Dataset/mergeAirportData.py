import csv
import json
import  pickle
from pymongo import MongoClient

with open('ufo_awesome.json',encoding="utf8") as json_data:
    ufo_data = json.load(json_data)
    print(len(ufo_data))
    print(ufo_data[0],type(ufo_data[0]))

db = MongoClient().ufo.cities
ufo_cities_dict = {}

count=0
for row in db.find():
    count+=1
    del row['_id']
    del row['region']
    if 'state' in row:
        del row['state']
    if 'country' in row:
        del row['country']
    location = row.pop('location')
    #print(location)
    ufo_cities_dict[location] = row
    #print(row)

print(ufo_cities_dict[' Huntington Beach, CA'])
#{'latitude': 33.6783336, 'longitude': -118.0000166, 'Nearest Airport': 'Civic Center Heliport', 'Distance': 0.03684175170069301}

compiled_list=[]
for row in ufo_data:
    if row['location'] in ufo_cities_dict:
        row.update(ufo_cities_dict[row['location']])
    compiled_list.append(row)

print(compiled_list[0])
#{'sighted_at': '19951009', 'reported_at': '19951009', 'location': ' Iowa City, IA', 'shape': '', 'duration': '', 'description': 'Man repts. witnessing &quot;flash, followed by a classic UFO, w/ a tailfin at back.&quot; Red color on top half of tailfin. Became triangular.', 'latitude': 41.6612561, 'longitude': -91.5299106, 'Nearest Airport': 'University of Iowa Hospitals & Clinic Heliport', 'Distance': 0.9246877620849214}
with open("compiled_list.pickle",'wb') as f:
    pickle.dump(compiled_list,f)