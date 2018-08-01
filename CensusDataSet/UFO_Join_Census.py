import csv
from collections import defaultdict

stateAbbr = {'AL':'Alabama','AK':'Alaska','AZ':'Arizona','AR':'Arkansas','CA':'California','CO':'Colorado',
'CT':'Connecticut','DC':'District of Columbia','DE':'Delaware','FL':'Florida','GA':'Georgia','HI':'Hawaii','ID':'Idaho','IL':'Illinois','IN':'Indiana',
'IA':'Iowa','KS':'Kansas','KY':'Kentucky','LA':'Louisiana','ME':'Maine','MD':'Maryland','MA':'Massachusetts','MI':'Michigan',
'MN':'Minnesota','MS':'Mississippi','MO':'Missouri','MT':'Montana','NE':'Nebraska','NV':'Nevada','NH':'New Hampshire',
'NJ':'New Jersey','NM':'New Mexico','NY':'New York','NC':'North Carolina','ND':'North Dakota','OH':'Ohio','OK':'Oklahoma',
'OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island','SC':'South Carolina','SD':'South Dakota',
'TN':'Tennessee','TX':'Texas','UT':'Utah','VT':'Vermont','VA':'Virginia','WA':'Washington','WV':'West Virginia',
'WI':'Wisconsin','WY':'Wyoming','PR':'Puerto Rico'}

StateCountyCities = {} #dictionary to store (stateShort, city) as key and value is county it belongs to
# from the data, we just have a available towns or cities under a county with no label whether it is a city or town
UFOStateYear ={} # dictionary with tuple (state, county , year) as key and value is count of sightings
CensusStateYear = {} # dictionary with tuple (state, county, year) as key and value is tuple of (population density, housing density)
ResultDict = defaultdict(list)
# dictionary with tuple (state, county, year) as key ,value list of [UFOSightingCount, population density, housing density]

#writing into the final merged output file
tsvout=open('../ufo_awesome_FINAL_OUTPUT.tsv', 'w')


with open('Input_2000Census.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader, None)
    next(reader,None)
    for row in reader:
        stateCounty = row['GCT_STUB.display-label_FQ'].split('-')
        if len(stateCounty) < 3:
            continue
        state = stateCounty[1].strip()
        tempcounty = stateCounty[2].strip()
        popDensity = float(row['HC08'].strip())
        houseDensity = float(row['HC09'].strip())
        if(popDensity > 1000 and houseDensity > 500):
            val = (popDensity,houseDensity, 'False' )  # Column false for urban area
        else:
            val = (popDensity,houseDensity, 'True' )   # Column True for rural area
        if 'County' in tempcounty:
            county = tempcounty.replace('County','').strip().lower()
        elif 'Municipio' in tempcounty:
            county = tempcounty.replace('Municipio','').strip().lower()
        elif 'Census Area' in tempcounty:
            county = tempcounty.replace('Census Area','').strip().lower()
        elif 'Borough' in tempcounty:
            county = tempcounty.replace('Borough','').strip().lower()
        elif 'City' in tempcounty:  # some cities are independent so County and City would be same E.g: Carson City, Nevada
            county = tempcounty.replace('City','').strip().lower()
        for y in range(1991, 2001):  # years from 1991 to 2000
            CensusStateYear[(state, county, y)] = val

with open('Input_2010Census.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader, None)
    next(reader,None)
    for row in reader:
        stateCounty = row['GCT_STUB.display-label_FQ'].split('-')
        if len(stateCounty) < 3:
            continue
        state = stateCounty[1].strip()
        tempcounty = stateCounty[2].strip()
        popDensity = float(row['SUBHD0401'].strip())
        houseDensity = float(row['SUBHD0402'].strip())
        if (popDensity > 1000 and houseDensity > 500):
            val = (popDensity, houseDensity, 'False')
        else:
            val = (popDensity, houseDensity, 'True')
        if 'County' in tempcounty:
            county = tempcounty.replace('County','').strip().lower()
        elif 'Municipio' in tempcounty:
            county = tempcounty.replace('Municipio','').strip().lower()
        elif 'Census Area' in tempcounty:
            county = tempcounty.replace('Census Area','').strip().lower()
        elif 'Borough' in tempcounty:
            county = tempcounty.replace('Borough','').strip().lower()
        elif 'City' in tempcounty:  # some cities are independent so County and City would be same E.g: Carson City, Nevada
            county = tempcounty.replace('City','').strip().lower()
        for y in range(2001, 2011):  # years from 2001 to 2010
            CensusStateYear[(state, county, y)] = val
#print(len(CensusStateYear.keys()))

#mapping city, state to county to map UFO sighting location to the respective county
with open('Input_CountyCitiesList.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader,None)
    for row in reader:
        temp = row['City|State short|State full|County|City alias'].split('|')
        # temp[0] is city, temp[1] is state Abr. temp[3] is County
        if 'City' in temp[4]:
            StateCountyCities[(temp[4].replace('City','').lower(),temp[1])] = temp[3]
        else:
            StateCountyCities[(temp[4].lower(), temp[1])] = temp[3].lower()

count = 0
with open('../ufo_airport_meteorite_scifi_merged.tsv') as tsvin:
    tsvreader = csv.reader(tsvin, delimiter='\t')
    header =  next(tsvreader, None)
    for col in header:
        tsvout.write(col + '\t')
    tsvout.write("County\tPopulation Density\tHousing Denisty\tRural?")
    #row[0]-- sighted at [1] reported at [2] location
    for row in tsvreader:
        tsvout.write('\n')
        for col in row:
            tsvout.write(col + '\t')
        year = int(row[0][0:4])
        if year == 0:
            year = int(row[1][0:4])
        location = row[2].split(",")
        stateInitial = location[1].strip()
        if(stateInitial not in stateAbbr.keys()): # this is to filter out invalid state e.g: location CANADA, BC (outside of U.S)
            tsvout.write('\n')
        else:
            state = stateAbbr[stateInitial]
            if 'County' in location[0]:
                county = location[0].replace('County', '').strip()
            else:
                if '(' in location[0]:
                    tempStr = location[0].split('(')[0].strip()
                else:
                    tempStr = location[0].strip()
                if 'City' in tempStr:
                    city = tempStr.replace('City', '').strip()
                else:
                    city = tempStr
                try:
                    county = StateCountyCities[(city.lower(), stateInitial)] # valid can be joined
                except:
                    count = count + 1  #to count invalid sighting locations which we could not map to a county
                    continue
            t = (state, county, year)
            if t in CensusStateYear.keys():
                tempval = CensusStateYear[t]
                tsvout.write(county + '\t' + str(tempval[0]) + '\t' + str(tempval[1]) + '\t' + tempval[2] + '\n')
            else:
                tsvout.write('\n')
                


print("Incorrect sighting locations which we could not map to a county : "+ str(count))





