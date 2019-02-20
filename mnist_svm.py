import csv
from sklearn import svm, metrics
from keras.datasets import mnist
import numpy as np
import pandas as pd

dataset = pd.read_csv('mnist_train.csv', delimiter=",", dtype=np.dtype('&gt;i4'))[1:]
labels = [x[0] for x in dataset]
data = [x[1:] for x in dataset]

n_samples = len(labels)
n_features = len(data[0])

print("Number of samples: " + str(n_samples) + ", number of features: "+ str(n_features))

classifier = svm.LinearSVC()

split_point = int(n_samples * 0.66)

labels_learn = labels[:split_point]
data_learn = data[:split_point]

labels_test = labels[split_point:]
data_test = data[split_point:]

print("Training: " + str(len(labels_learn)) + "Test: " + str(len(labels_test)))

classifier.fit(data_learn, labels_learn)

predicted = classifier.predict(data_test)

print("Classification report for classifier %s:n%sn"%(classfier, metrics.classification_report(labels_test, predicted)))

print("Confusion matrix:n%s" % metrics.confusion_matrix(labels_test, predicted))