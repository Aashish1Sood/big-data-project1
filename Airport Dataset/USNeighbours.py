# This code is to generate the neighbouring states dictionary.
import csv
import pickle
fname = "neighbour states.csv"

us_neighbours = open(fname, "r",encoding="UTF-8")
us_nb = csv.reader(us_neighbours)
neighbour_dict = {}

for i,row in enumerate(us_nb):
    a,b = "US-"+row[0],"US-"+row[1]
    if a not in neighbour_dict:
        neighbour_dict[a] = [b]
    else:
        neighbour_dict[a].append(b)
    if b not in neighbour_dict:
        neighbour_dict[b] = [a]
    else:
        neighbour_dict[b].append(a)

with open("neighbour_dict.pickle", 'wb') as f1:
    pickle.dump(neighbour_dict, f1)
