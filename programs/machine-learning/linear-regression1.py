#!/usr/bin/env python

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")
# Since our data is seperated by semicolons we need to do sep=";"

print(data.head())

data=data[["G1","G2","G3",'failures','studytime','absences']]
print(data.head())


predict=G3
x=np.array(data.drop(['predict'],1))
y=np.array(data['predict'])
