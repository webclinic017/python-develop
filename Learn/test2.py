import random
from sklearn import neighbors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

x1 = np.random.normal(50, 6, 200)
y1 = np.random.normal(5, 0.5, 200)

x2 = np.random.normal(30,6,200)
y2 = np.random.normal(4,0.5,200)

x3 = np.random.normal(45,6,200)
y3 = np.random.normal(2.5, 0.5, 200)

plt.scatter(x1,y1,c='b',marker='s',s=50,alpha=0.8)
plt.scatter(x2,y2,c='r', marker='^', s=50, alpha=0.8)
plt.scatter(x3,y3, c='g', s=50, alpha=0.8)

#plt.show()
############

x_val = np.concatenate((x1,x2,x3))
y_val = np.concatenate((y1,y2,y3))

x_diff = max(x_val)-min(x_val)
y_diff = max(y_val)-min(y_val)

x_normalized = [x/(x_diff) for x in x_val]
y_normalized = [y/(y_diff) for y in y_val]
xy_normalized = list(zip(x_normalized,y_normalized))
plt.scatter(x_normalized,y_normalized)
#plt.show()
##########

labels = [1]*200+[2]*200+[3]*200
#print(labels)

clf = neighbors.KNeighborsClassifier(n_neighbors=30,weights="uniform",algorithm="auto")

#print(xy_normalized)
clf.fit(xy_normalized, labels)

nearests = clf.kneighbors([(50/x_diff, 5/y_diff),(30/x_diff, 3/y_diff)], 10, False)
prediction = clf.predict([(50/x_diff, 5/y_diff),(30/x_diff, 3/y_diff)])
print(prediction)

prediction_proba = clf.predict_proba([(50/x_diff, 5/y_diff),(30/x_diff, 3/y_diff)])
print(prediction_proba)


x1_test = np.random.normal(50, 6, 100)
y1_test = np.random.normal(5, 0.5, 100)

x2_test = np.random.normal(30,6,100)
y2_test = np.random.normal(4,0.5,100)

x3_test = np.random.normal(45,6,100)
y3_test = np.random.normal(2.5, 0.5, 100)

xy_test_normalized = list(zip(np.concatenate((x1_test,x2_test,x3_test))/x_diff,\
                        np.concatenate((y1_test,y2_test,y3_test))/y_diff))

labels_test = [1]*100+[2]*100+[3]*100

score = clf.score(xy_test_normalized, labels_test)
print(score)







'''
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
import pandas as pd
import statsmodels.api as sm

nsample=100
x=np.linspace(0,10,nsample)
#print(x)
X = np.column_stack((x, x**2))
X=sm.add_constant(X)
#print(X)
beta=np.array([1,0.1,10])
e = np.random.normal(size=nsample)
#print(e)
print(X.shape)
print(beta.shape)
y = np.dot(X, beta)+e
#plt.plot(x,y)
#plt.show()
model=sm.OLS(y,X)
results = model.fit()
print(results.params)
#print(results.summary())
y_fitted = results.fittedvalues
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'o', label='data')
ax.plot(x, y_fitted, 'r--.',label='OLS')
ax.legend(loc='best')
#ax.axis((-0.05, 2, -1, 25))
plt.show()
'''
