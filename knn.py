#-------------------------------------------------------------------------
# AUTHOR: Jonathan Lu
# FILENAME: knn.py
# SPECIFICATION: This program reads a csv file to find the error rate using KNN method
# FOR: CS 4200- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
correct = 0
incorrect = 0

#reading the data in a csv file
with open('C:/Users/Administrator/Desktop/binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
    #--> add your Python code here
    # X =
    X = []
    for j, row in enumerate(db):
        if i == j:
            continue
        newRow = []
        for val in row[:-1]:
            newRow.append(int(val))
        X.append(newRow)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
    #--> add your Python code here
    # Y =
    Y = []
    for j, row in enumerate(db):
            if i == j:
                continue
            elif row[-1] == '+':
                Y.append(1)
            elif row[-1] == '-':
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    testSample = [int(instance[0]), int(instance[1])]
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)
    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]
    test = 0
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if instance[2] == '+':
        test = 1
    elif instance[2] == '-':
        test = 2
    else:
        test = -1
    if class_predicted == test:
        correct += 1
    else:
        incorrect += 1

#print the error rate
#--> add your Python code here
error_rate = incorrect/(correct+incorrect)

print('X = ' + str(X))
print('Y = ' + str(Y))
print('Error Rate: ', error_rate, '%')


