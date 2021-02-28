#-------------------------------------------------------------------------
# AUTHOR: Jonathan Lu
# FILENAME: decision_tree.py
# SPECIFICATION: This program reads csv files to calculate the accuracy of their decision tree
# FOR: CS 4200- Assignment #2
# TIME SPENT: 3 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['C:/Users/Administrator/Desktop/contact_lens_training_1.csv', 'C:/Users/Administrator/Desktop/contact_lens_training_2.csv', 'C:/Users/Administrator/Desktop/contact_lens_training_3.csv']
totalAccuracy = []
for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    age = ['Young', 'Prepresbyopic', 'Presbyopic']
    spectacle = ['Myope', 'Hypermetrope']
    astigmatism = ['Yes', 'No']
    tear = ['Reduced', 'Normal']
    lense = ['Yes', 'No']
    attributes = []
    attributes.append(age)
    attributes.append(spectacle)
    attributes.append(astigmatism)
    attributes.append(tear)
    attributes.append(lense)

    for i, row in enumerate(dbTraining):
      newRow = []
      for j, value in enumerate(row[:-1]):
        newRow.append(attributes[j].index(value) + 1)
      X.append(newRow)

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here

    for row in dbTraining:
      if row[-1] == 'Yes':
        Y.append(1)
      elif row[-1] == 'No':
        Y.append(2)

    lowestAccuracy = 1

    #loop your training and test tasks 10 times here
    for i in range (10):
      #fitting the decision tree to the data setting max_depth=3
      clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
      clf = clf.fit(X, Y)

      #read the test data and add this data to dbTest
      #--> add your Python code here
      dbTest = []
      with open('C:/Users/Administrator/Desktop/contact_lens_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                dbTest.append (row)

      correct = 0
      incorrect = 0
      for data in dbTest:
          #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
          #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
          #--> add your Python code here
          transformData = []
          for j, value in enumerate(data):
            transformData.append(attributes[j].index(value) + 1)
            
          class_predicted = clf.predict([transformData[:-1]])[0]
          #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
          #--> add your Python code here
          if transformData[4] == class_predicted:
            correct+=1
          else:
            incorrect+=1

      #find the lowest accuracy of this model during the 10 runs (training and test set)
      #--> add your Python code here
      accuracy = correct/(correct+incorrect)
      if accuracy < lowestAccuracy:
           lowestAccuracy = accuracy
    totalAccuracy.append(lowestAccuracy)

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:
         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here
print('X = ' + str(X))
print('Y = ' + str(Y))
print('final accuracy when training on contact_lens_training_1.csv:' + str(totalAccuracy[0]))
print('final accuracy when training on contact_lens_training_2.csv:' + str(totalAccuracy[1]))
print('final accuracy when training on contact_lens_training_3.csv:' + str(totalAccuracy[2]))
    



