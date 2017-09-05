from sklearn import svm
import numpy as np
import os
import csv

# The class that makes the processing
class SVM():
  def __init__(self):
    path = os.path.dirname(os.path.realpath(__file__))
    standardPath = path + "/Dataset/SMV/Standar.csv"
    categoriesPath = path + "/Dataset/SMV/Categories.txt"
    
    # opens the standard training file 
    csvStandardTraining = open(standardPath, 'r')

    # open and read the categories
    categoriesFile = open(categoriesPath)
    categoriesFileLines = [line.rstrip('/n') for line in categoriesFile]
    self.y = [int(x) for x in categoriesFileLines]  # String to Int
    
    self.X = []
    index = 0
    for row in csv.reader(csvStandardTraining, delimiter=';'):
      if index !=0:
        # 1;2;3;4 -> [1,2,3,4]
        arr = list(map(int, [i.replace(".", "") for i in row]))
        # [[1,2,3,4], [1,2,3,4]]
        self.X.append(arr)
      else: 
        self.X.append([0,0,0,0])

      index=index+1

    # train the classifier
    self.classifier = svm.SVC()    
    self.classifier.fit(self.X, self.y)

  def predict(self, target):
    target = np.array(target).reshape(1,-1)
    return self.classifier.predict(target)
