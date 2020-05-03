#!/usr/bin/env python
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data=pd.read_csv("student-mat.csv",sep=';')

data=data[["G1","G2","G3",'failures','studytime','absences']]
print(data.head())
