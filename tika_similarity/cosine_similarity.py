import tika
tika.initVM()
import pickle
import csv
from vector import Vector

# Unpickling dataset of features
dataDict = pickle.load( open( "featureDictVer2.p", "rb" ) )

feature1 = "Distance"
listOfDict = []
featKeys = dataDict.keys()

#Preparing list of rows with features and value mapping where Key is the feature and Value is the value of the feature on that particular row
for i in range(0, len(dataDict[feature1])):
    dict = {}
    for j in range(0, len(featKeys)):
        dict[featKeys[j]] = dataDict[featKeys[j]][i]
    listOfDict.append(dict)


# Computing Cosine_simiilarity based on the algorithm provided in cosine_similarity.py in tika_similarity
with open("cosine_similarity.csv", "w") as outF:
    a = csv.writer(outF, delimiter=',')
    a.writerow(["x-coordinate" ,"y-coordinate" ,"Similarity_score"])

    for key1 in range(0, 20):
        for key2 in range(key1+1, key1+20):
            if key1 == key2:
                continue


            row1 = "Meteorite"+str(listOfDict[key1]["Meteor possibility"])
            row1 = row1 + "Sci-fi"+str(listOfDict[key1]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row1 = row1 + "isRural" + str(listOfDict[key1]["Rural?"])

            row2 = "Meteorite" + str(listOfDict[key2]["Meteor possibility"])
            row2 = row2 + "Sci-fi" + str(
                listOfDict[key2]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row2 = row2 + "isRural" + str(listOfDict[key2]["Rural?"])


            row_cosine_distance = [row1,row2]

            file_edit_distance = 0.0
            count = 0
            v1 = Vector(key1 + 1, listOfDict[key1])
            v2 = Vector(key2 + 1, listOfDict[key2])

            row_cosine_distance.append(v1.cosTheta(v2))

            a.writerow(row_cosine_distance)

        if (key1 % 100 == 0):
            print(key1)
