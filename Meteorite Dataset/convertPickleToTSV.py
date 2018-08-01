import csv
import json
import  pickle

with open("compiled_list_1.pickle",'rb') as f:
    c_list = pickle.load(f)

f = open("../ufo_airport_meteorite.tsv","w",encoding="UTF-8")

count = 0
for item in c_list:
    f_string=""
    if 'sighted_at' in item:
        f_string=f_string + str(item['sighted_at'])
    f_string = f_string+ '\t'
    if 'reported_at' in item:
        f_string=f_string + str(item['reported_at'])
    f_string = f_string+ '\t'
    if 'location' in item:
        f_string=f_string + str(item['location'])
    f_string = f_string+ '\t'
    if 'shape' in item:
        f_string=f_string + str(item['shape'])
    f_string = f_string+ '\t'
    if 'duration' in item:
        f_string=f_string + str(item['duration'])
    f_string = f_string+ '\t'
    if 'description' in item:
        f_string=f_string + str(item['description'])
    f_string = f_string+ '\t'
    if 'latitude' in item:
        f_string=f_string + str(item['latitude'])
    f_string = f_string+ '\t'
    if 'longitude' in item:
        f_string=f_string + str(item['longitude'])
    f_string = f_string+ '\t'
    if 'Nearest Airport' in item:
        f_string=f_string + str(item['Nearest Airport'])
    f_string = f_string+ '\t'
    if 'Distance' in item:
        if item['Distance'] <=25:
            count+=1
        f_string=f_string + str(item['Distance'])
    f_string = f_string+ '\t'
    if 'meteor_name' in item:
        f_string=f_string + str(item['meteor_name'])
    f_string = f_string+ '\t'
    if 'meteor_distance' in item:
        f_string=f_string + str(item['meteor_distance'])
    f_string = f_string+ '\t'
    if 'm_possibility' in item:
        f_string=f_string + str(item['m_possibility'])
    f_string = f_string+ '\n'
    f.write(f_string)
f.close()
