#-------------------------------------------------------------------------
# AUTHOR: Jonathan Lu
# FILENAME: naive_bayes.py
# SPECIFICATION: This program opens a csv file and will predict the confidence of playing tennis
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

weather_training = []
#reading the training data
#--> add your Python code here
with open('C:/Users/Administrator/Desktop/weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         weather_training.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []
outlook = ['Sunny', 'Overcast', 'Rain']
temp = ['Hot', 'Mild', 'Cool']
humidity = ['High', 'Normal']
wind = ['Weak', 'Strong']
attributes = []
attributes.append(outlook)
attributes.append(temp)
attributes.append(humidity)
attributes.append(wind)

for i, row in enumerate(weather_training):
    newRow = []
    for j, value in enumerate(row[1:-1]):
        newRow.append(attributes[j].index(value) + 1)
    X.append(newRow)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []
for row in weather_training:
      if row[-1] == 'Yes':
        Y.append(1)
      elif row[-1] == 'No':
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
weather_test = []
with open('C:/Users/Administrator/Desktop/weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         weather_test.append (row)

X2 = []
for i, row in enumerate(weather_test):
    newRow = []
    for j, value in enumerate(row[1:-1]):
        newRow.append(attributes[j].index(value) + 1)
    X2.append(newRow)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
predictions = clf.predict(X2)

for i, row in enumerate(X2):
    confidence = clf.predict_proba([row])[0]
    if confidence[0] >= 0.75:
        prediction = ''
        if predictions[i] == 1:
            prediction = 'yes'
        elif predictions[i] == 2:
            prediction = 'no'
        print(weather_test[i][0].ljust(15) + weather_test[i][1].ljust(15) + weather_test[i][2].ljust(15) 
              + weather_test[i][3].ljust(15) + weather_test[i][4].ljust(15) + prediction.ljust(15) + str(confidence[0]).ljust(15))