import json
import csv
with open('../ufo_awesome.json',encoding = "utf-8") as json_data:
    ufo_data = json.load(json_data)
    print(len(ufo_data))

yearDict = {}
#test = int(ufo_data[0]['sighted_at'][0:4])
#print (type(test))

print ()
for r in ufo_data:
    year = int(r['sighted_at'][0:4])
    if year ==0:
        year = int(r['reported_at'][0:4])
    if year in yearDict.keys():
        yearDict[year] = yearDict[year]+1
    else:
        if year == 0:
            print(year)
            print(r)
        yearDict[year]= 1

abc = open("output_UFOCountByYear.tsv",'w')
abc.write("Year Count\n")
s = [(k, yearDict[k]) for k in sorted(yearDict, key=yearDict.get, reverse=True)]
for k, v in s:
    abc.write(str(k)+"  "+str(v)+"\n")

