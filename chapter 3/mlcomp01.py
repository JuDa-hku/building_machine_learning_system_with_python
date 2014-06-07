import os
import sys
import sklearn.datasets
import scipy as sp

from utils import DATA_DIR

if not os.path.exists(DATA_DIR):
    print("""\
         Have not downloaded the data set in %s.""" %DATA_DIR)
    sys.exit(1)
    
new_post = \
           """Disk drive problems. Hi, I have a problem with my hard idsk.
           After 1 year it is working only sporadically now.
           I tried to format it, but now it doesn't boot any more.
           Any ideas? Thanks."""

groups = [
'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
dataset = sklearn.datasets.load_mlcomp("20news-18828", "train",
                                       mlcomp_root=DATA_DIR,
                                       categories=groups)

print("Number of posts:", len(dataset.filenames))

labels = dataset.target
num_clusters = 50

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')

from sklearn.feature_extraction.text import TfidfVectorizer

class StemmedTfidfVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5,
                                    stop_words='english', charset_error='ignore'
                                    )
vectorized = vectorizer.fit_transform(dataset.data)        
num_samples, num_features = vectorized.shape
print("#samples: %d, #features: %d" %(num_samples, num_features))

from sklearn.cluster import KMeans

km = KMeans(n_clusters=num_clusters, init='k-means++', n_init=1,
            verbose=1)
clustered = km.fit(vectorized)


new_post_vec = vectorizer.transform([new_post])
new_post_label = km.predict(new_post_vec)[0]

similar_indices = (km.labels_ == new_post_label).nonzero()[0]

similar = []
for i in similar_indices:
    dist = sp.linalg.norm((new_post_vec - vectorized[i]).toarray())
    similar.append((dist, dataset.data[i]))

similar = sorted(similar)

show_at_1 = similar[0]
show_at_2 = similar[1]
show_at_3 = similar[2]

print("===#1===")
print(show_at_1)
print()

print("===#2===")
print(show_at_2)
print()

print("===#3===")
print(show_at_3)
print()



