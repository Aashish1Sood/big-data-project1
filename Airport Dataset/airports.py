#This code is to capture all the airports based on the region of the location.
import csv
import operator
import pickle

airport_db = open('airports.csv', "r",encoding="UTF-8")
airport = csv.reader(airport_db)
#Total countires is 244
#Below is the list of country codes with more than 200 airports
#[('US', 22389), ('BR', 4188), ('CA', 2781), ('AU', 1959), ('RU', 1025), ('DE', 934), ('GB', 863), ('FR', 839), ('AR', 827), ('MX', 808), ('CO', 706), ('IT', 664), ('VE', 592), ('PG', 591), ('KR', 539), ('ZA', 481), ('CL', 474), ('ID', 466), ('ES', 404), ('CN', 382), ('KE', 368), ('IN', 338), ('CD', 285), ('PH', 279), ('CZ', 267), ('PL', 255), ('NA', 246), ('JP', 233), ('NO', 223), ('SE', 218), ('NZ', 209), ('TZ', 207),
airport_dict = {}
count = 0
for row in airport:
    if count == 0:
        count +=1
        continue
    country_code = row[8]
    region_code = row[9]
    name = row[3]
    lat = float(row[4])
    long = float(row[5])
    record = [name,lat,long]
    print(record)
    if country_code == "US":
        if region_code not in airport_dict:
            airport_dict[region_code] = [record]
        else:
            airport_dict[region_code].append(record)
    else:
        if country_code not in airport_dict:
            airport_dict[country_code] = [record]
        else:
            airport_dict[country_code].append(record)
with open("airport_data.pickle",'wb') as f:
    pickle.dump(airport_dict,f)


