from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

#load the data with function load_iris()
data=load_iris()
features=data['data']
feature_name=data['feature_names']
target=data['target']

for t, marker, c in zip(xrange(3), ">ox", "rgb"):
    #plot each class on its own
    plt.scatter(features[target==t, 3],
    features[target==t,2],
    marker=marker,
    c=c)

plt.xlabel("feature 0")
plt.ylabel("feature 2")
#plt.show() shows feature 2 is useful
dir(data)
data.feature_names
data.target_names

plength=features[:, 2]
##get setosa features

is_setosa = (data.target==0)
max_setosa = plength[is_setosa].max()
min_non_setosa=plength[~is_setosa].min()
print('Maximum of setosa: {0}.' .format(max_setosa)) 
print('Minimum of others: {0}.' .format(min_non_setosa))

#to seprate the other two
features=features[~is_setosa]
virginica=(data.target==2)
best_acc=-1.0
target=data.target[~is_setosa]
target=target-1
for fi in xrange(features.shape[1]):
    #generate all possible threshold for this feature
    thresh=features[:, fi].copy()
    thresh.sort()
    for t in thresh:
        pred = np.array(features[:,fi]>t)
        acc = np.array(target==pred).mean()
        if acc>best_acc:
            best_acc=acc
            best_fi=fi
            best_t=t
print ("best_acc=%f, besit_fi=%f, best_t=%f" %(
    best_acc, best_fi, best_t))

#if example[best_fi]>t:
#    print 'virginica'
#else:
#    print 'versicolor'