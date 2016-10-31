import pandas as pd
import numpy as np
column_names=['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Base Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names=column_names)
data=data.replace(to_replace='?',value=np.nan)
data=data.dropna(how='any')
data.shape
