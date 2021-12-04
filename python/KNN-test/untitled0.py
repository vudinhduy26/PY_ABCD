# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:54:11 2021

@author: duy
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print('Number of classes : ',len(np.unique(iris_y)))
print('Number of data point : ',len(iris_y))

X0 = iris_X[iris_y == 0,:]
print('Samples from class 0 : \n',X0[:5,:])

X1 = iris_X[iris_y == 1,:]
print('\nSamples from class 1:\n', X1[:5,:])

X2 = iris_X[iris_y == 2,:]
print('\nSamples from class 2:\n', X2[:5,:])

#Tách training và test sets
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=50)
print("Training size: ",len(y_train))
print("Test size    : ",len(y_test))

clf = neighbors.KNeighborsClassifier(n_neighbors = 5 ,p=2 , weights = 'distance')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Print results for 20 test data points: \n")
print("Predicted labels: ", y_pred[20:40])
print("Ground truth    : ", y_test[20:40])

print('\n Accuracy of 1NN : ',100*accuracy_score(y_test,y_pred))