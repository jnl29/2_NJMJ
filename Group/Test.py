import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection, metrics, preprocessing
from sklearn.decomposition import PCA
from sklearn import tree

import matplotlib.pyplot as plt
from sklearn.externals.six import StringIO
#import pydotplus
from IPython.display import Image


raw_df = pd.read_csv('housingdata.csv')
print (raw_df.drop(columns=['Alley','PoolQC','Fence','MiscFeature']))
