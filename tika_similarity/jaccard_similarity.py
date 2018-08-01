import tika
tika.initVM()
import pickle
import csv



def stringify(attribute_value):
    if isinstance(attribute_value, list):
        return str((", ".join(attribute_value)).encode('utf-8').strip())
    else:
        return str(attribute_value.encode('utf-8').strip())

# Unpickling dataset of features
dataDict = pickle.load( open( "featureDictVer2.p", "rb" ) )

listOfDict = []
feature1 = "Distance"
featKeys = dataDict.keys()

#Preparing list of rows with features and value mapping where Key is the feature and Value is the value of the feature on that particular row
for i in range(0, len(dataDict[feature1])):
    dict = {}
    for j in range(0, len(featKeys)):
        dict[featKeys[j]] = dataDict[featKeys[j]][i]
    listOfDict.append(dict)


# Computing Jaccard_simiilarity based on the algorithm provided in jaccard_similarity.py in tika_similarity
with open("jaccard_similarity.csv", "w") as outF:
    a = csv.writer(outF, delimiter=',')
    a.writerow(["x-coordinate" ,"y-coordinate" ,"Similarity_score"])

    for key1 in range(0, 20):
        for key2 in range(key1+1, key1+20):
            if key1 == key2:
                continue
            isCoExistant = lambda k: (k in listOfDict[key2]) and (listOfDict[key1][k] == listOfDict[key2][k]) and (k != "description")
            intersection = reduce(lambda m, k: (m + 1) if isCoExistant(k) else m, listOfDict[key1].keys(), 0)

            union = len(listOfDict[key1].keys()) + len(listOfDict[key2].keys()) - intersection
            jaccard = float(intersection) / union

            row1 = "Meteorite"+str(listOfDict[key1]["Meteor possibility"])
            row1 = row1 + "Sci-fi"+str(listOfDict[key1]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row1 = row1 + "isRural" + str(listOfDict[key1]["Rural?"])

            row2 = "Meteorite" + str(listOfDict[key2]["Meteor possibility"])
            row2 = row2 + "Sci-fi" + str(
                listOfDict[key2]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row2 = row2 + "isRural" + str(listOfDict[key2]["Rural?"])

            a.writerow([row1, row2, jaccard])

        if (key1 % 100 == 0):
            print(key1)
