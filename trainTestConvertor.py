# Importing necessary modules.
import re
import os

# Loading postive and negative review data from respective directories.
# Change "path" to respective directory !

path = '/home/khushvirmani/Desktop/movieReviewProject/aclImdb/'


posTrainData = os.listdir(path + 'train/pos')
nesTrainData = os.listdir(path + '/train/neg')
posTestData = os.listdir(path + 'test/pos')
negTestData = os.listdir(path + 'test/neg')

# Making regular expression object.
_nsre = re.compile('([0-9]+)')

# Sorting key for aligning the data.
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)] 


posTrainData.sort(key = natural_sort_key)
negTrainData.sort(key = natural_sort_key)
posTestData.sort(key = natural_sort_key)
negTestData.sort(key = natural_sort_key)


trainX = open("imdbTrainX.txt", 'w')
trainY = open("imdbTrainY.txt", "w")
testX = open("imdbtestX.txt", 'w')
testY = open("imdbtestY.txt", "w")

# Creating clean text files for processing.  
#
for ix in range(len(posTrainData)):
    f = open(path + "train/pos/" + posTrainData[ix], "r")
    sent = f.readlines()
    trainX.write( " ".join(sent) + "\n")
    rating = posTrainData[ix]
    ratedVal = rating[rating.index("_")+1 : -4]
    trainY.write(ratedVal + "\n")

for ix in range(len(negTrainData)):
    g = open(path + "train/neg/" + negTrainData[ix], "r")
    line = g.readlines()
    trainX.write(" ".join(line) + "\n")
    rating = negTrainData[ix]
    ratedVal = rating[rating.index("_")+1 : -4]
    trainY.write(ratedVal + "\n")


for ix in range(len(posTestData)):
    f = open(path + "test/pos/" + posTestData[ix], "r")
    sent = f.readlines()
    testX.write( " ".join(sent) + "\n")
    rating = posTestData[ix]
    ratedVal = rating[rating.index("_")+1 : -4]
    testY.write(ratedVal + "\n")

for ix in range(len(negTestData)):
    g = open(path + "test/neg/" + negTestData[ix], "r")
    line = g.readlines()
    testX.write(" ".join(line) + "\n")
    rating = negTestData[ix]
    ratedVal = rating[rating.index("_")+1 : -4]
    testY.write(ratedVal + "\n")

trainX.close()
trainY.close()
testX.close()
testY.close()
