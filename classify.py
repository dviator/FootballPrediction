#!/usr/bin/python

# from makeNFLdata import makeNFLdata
from average import movingAvgData
import matplotlib.pyplot as plt

# features_train, labels_train, features_test, labels_test = makeNFLdata()
features_train, labels_train, features_test, labels_test = movingAvgData()

# Use K-nearest-neighbors algorithm to train/test our classifier 
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3, weights='distance')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

print "the accuracy is : ", accuracy

#### Initial Visualization ##############################################
passing_yd_win 	= [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]=='W']
passing_yd_loss	= [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]=='L']
rushing_yd_win	= [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]=='W']
rushing_yd_loss	= [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]=='L']
passing_td_win	= [features_train[ii][2] for ii in range(0, len(features_train)) if labels_train[ii]=='W']
passing_td_loss	= [features_train[ii][2] for ii in range(0, len(features_train)) if labels_train[ii]=='L']
rushing_td_win	= [features_train[ii][3] for ii in range(0, len(features_train)) if labels_train[ii]=='W']
rushing_td_loss	= [features_train[ii][3] for ii in range(0, len(features_train)) if labels_train[ii]=='L']

passing_yd_pred_win 	= [features_test[ii][0] for ii in range(0, len(features_test)) if pred[ii]=='W']
passing_yd_pred_loss	= [features_test[ii][0] for ii in range(0, len(features_test)) if pred[ii]=='L']
rushing_yd_pred_win		= [features_test[ii][1] for ii in range(0, len(features_test)) if pred[ii]=='W']
rushing_yd_pred_loss	= [features_test[ii][1] for ii in range(0, len(features_test)) if pred[ii]=='L']

plt.xlim(-200.0, 200.0) #passing_yds in x-dim
plt.ylim(-150, 150.0) #rushing-yds in y-dim
plt.scatter(passing_yd_win, rushing_yd_win, color = "b", label="win")
plt.scatter(passing_yd_loss, rushing_yd_loss, color = "r", label="loss")
plt.scatter(passing_yd_pred_win, rushing_yd_pred_win, color = "g", label="predicted win")
plt.scatter(passing_yd_pred_loss, rushing_yd_pred_loss, color = "y", label="predicted loss")
plt.legend()
plt.xlabel("passing yds")
plt.ylabel("rushing yds")
plt.show()