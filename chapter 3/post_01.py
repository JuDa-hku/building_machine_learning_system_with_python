import os
import sys

import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer

from utils import DATA_DIR

print os.getcwd()
TOY_DIR = os.path.join(DATA_DIR, "toy")
posts = [open(os.path.join(TOY_DIR,f)).read() for f in os.listdir(TOY_DIR)]
