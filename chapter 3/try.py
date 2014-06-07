import os
import sklearn
from utils import DATA_DIR

TOY_DIR = os.path.join(DATA_DIR, "toy")
posts = [open(os.path.join(TOY_DIR, f)).read() for f in
         os.listdir(TOY_DIR)]
print TOY_DIR
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #feature: %d" %(num_samples,
                                    num_features))
print(vectorizer.get_feature_names())
new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
#coo_matrix to store data, as most of them are zero
print(new_post_vec)
print(new_post_vec.toarray())

import scipy as sp
def dist(v1, v2):
    delta=v1-v2
    return sp.linalg.norm(delta.toarray())

def dist_norm(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized-v2_normalized
    return sp.linalg.norm(delta.toarray())


import sys
##iterate over all the posts and remember the nearest one
best_doc=None
best_dist=sys.maxint
best_i=None
for i in range(0, num_samples):
    post=posts[i]
    if post==new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print "=== Post %i with dist=%.2f: %s" %(i, d, post)
    if d<best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" %(best_i, best_dist))

## find a way to remove stop words which show up quite often
## for example "the" "a" "and"
vectorizer = CountVectorizer(min_df=1, stop_words='english')
X_train=vectorizer.fit_transform(posts)
sorted(vectorizer.get_stop_words())[:20]
print X_train.toarray()
print vectorizer.get_feature_names()
new_post_vec = vectorizer.transform([new_post])
best_doc=None
best_dist=sys.maxint
best_i=None
for i in range(0, num_samples):
    post=posts[i]
    if post==new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print "=== Post %i with dist=%.2f: %s" %(i, d, post)
    if d<best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" %(best_i, best_dist))

#we need a function that reduces words to their specific word item
# Natural Language Toolkit provides a stemmer that can be plugged into CountVectorizer
import nltk.stem
s = nltk.stem.SnowballStemmer('english')
print s.stem("graphics")
print s.stem("imaging")
##output imag
print s.stem("buys")==s.stem("buying")

english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
        
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
X_train = vectorizer.fit_transform(posts)
new_post_vec = vectorizer.transform([new_post])

for i in range(0, num_samples):
    post=posts[i]
    if post==new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print "=== Post %i with dist=%.2f: %s" %(i, d, post)
    if d<best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" %(best_i, best_dist))