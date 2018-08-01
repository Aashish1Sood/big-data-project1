import tika
tika.initVM()
import editdistance
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
featKeys = dataDict.keys()
feature1 = "Distance"

#Preparing list of rows with features and value mapping where Key is the feature and Value is the value of the feature on that particular row
for i in range(0, len(dataDict[feature1])):
    dict = {}
    for j in range(0, len(featKeys)):
        dict[featKeys[j]] = dataDict[featKeys[j]][i]
    listOfDict.append(dict)

# Computing EditDistance_simiilarity based on the algorithm provided in edit-value-similarity.py in tika_similarity
with open("edit_similarity.csv", "w") as outF:
    a = csv.writer(outF, delimiter=',')
    a.writerow(["x-coordinate", "y-coordinate", "z-coordinate", "Similarity_score"])

    for key1 in range(0, 20):
        for key2 in range(key1+1, key1+20):
            if key1 == key2:
                continue

            row1 = "Meteorite" + str(listOfDict[key1]["Meteor possibility"])
            row1 = row1 + "Sci-fi" + str(
                listOfDict[key1]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row1 = row1 + "isRural" + str(listOfDict[key1]["Rural?"])

            row2 = "Meteorite" + str(listOfDict[key2]["Meteor possibility"])
            row2 = row2 + "Sci-fi" + str(
                listOfDict[key2]["Possibility of ufo_sighting being a delusion after a sci-fi movie being released?"])
            row2 = row2 + "isRural" + str(listOfDict[key2]["Rural?"])

            rowToWrite = [row1, row2]

            featLen = len(listOfDict[key1])
            file_edit_distance = 0.0
            for k in listOfDict[key1].keys():
                if k == "description":
                    continue
                file1_feature_value = stringify(listOfDict[key1][k])
                file2_feature_value = stringify(listOfDict[key2][k])

                if len(file1_feature_value) == 0 and len(file2_feature_value) == 0:
                    feature_distance = 0.0
                else:

                    feature_distance = float(editdistance.eval(file1_feature_value, file2_feature_value)) / (
                        len(file1_feature_value) if len(file1_feature_value) > len(file2_feature_value) else len(
                            file2_feature_value))

                file_edit_distance += feature_distance

            file_edit_distance /= float(featLen)

            rowToWrite.append(1 - file_edit_distance)
            a.writerow(rowToWrite)
