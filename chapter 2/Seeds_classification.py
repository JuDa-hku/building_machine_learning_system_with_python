#the goal of a good feature are to simultanesously vary with what matters and be invariant with what does not. It might be hard to achieve both objectives perfectly, but we want to approximate this ideal.
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

data=sp.genfromtxt("Seeds_data")
labels=data[:,7]
features=data[:,range(7)]
area=data[:, 0]
compa=data[:, 2]

np.random.shuffle(data)
training=data[range(int(data.shape[0]*0.9)),:]
# use the whole set as training set, accu will be 1
testing=data[range(int(data.shape[0]*0.9), data.shape[0]),:]
training_set=training[:,range(7)]
testing_set=testing[:, range(7)]
training_labels=training[:,7]
testing_labels=testing[:, 7]


def distance(p0, p1):
    'Computes squared euclidean distance'
    return np.sum( (p0-p1)**2)

def nn_classify(training_set, training_labels, new_example):
    dists=np.array([distance(t, new_example)
                for t in training_set])
    nearest=dists.argmin()
    return training_labels[nearest]

pre=np.array([nn_classify(training_set, training_labels,
                     x) for x in testing_set])

print np.array(pre==testing_labels).mean()
labels=labels-1
for t, marker, c in zip(xrange(3), ">ox", "rgb"):
    plt.scatter(area[labels==t],
    compa[labels==t],
    marker=marker,
    c=c)
plt.show()
