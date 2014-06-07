import os
import sys
DATA_DIR = os.path.join(
os.path.dirname(os.path.realpath(__file__)), "data")
CHART_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pic")
if not os.path.exists(DATA_DIR):
    print(" not exist")
    sys.exit(1)