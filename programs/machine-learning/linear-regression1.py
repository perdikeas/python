#!/usr/bin/env python




class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


data = pd.read_csv("student-mat.csv", sep=";")
# Since our data is seperated by semicolons we need to do sep=";"



data=data[["G1","G2","G3",'failures','studytime','absences']]
print(data.head())

print(data['studytime'])

predict="G3"

#training data
x=np.array(data.drop([predict],1))
y=np.array(data[predict])

best=0
#train test split model
for i in range(50):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    linear=linear_model.LinearRegression()
    linear.fit(x_train,y_train)
    acc=linear.score(x_test,y_test)



    if acc>best:
        best=acc
        print(Color.RED+Color.BOLD+'Accuracy is now: {}'.format(acc))
        #this creates a new file named f in which we saved our linear regression model
        with open("student-grades.pickle","wb") as f:
            pickle.dump(linear,f)


pickle_contents=open("student-grades.pickle","rb")


#we load the pickle model which we saved into the linear regression model
#by doing this we do not need to train our model each time
linear=pickle.load(pickle_contents)


predictions=linear.predict(x_test)


print("\n\n\n\n\n")
for x in range(len(predictions)):
    print( predictions[x], x_test[x], y_test[x])

print("\n\n\n\n")

independant_variable='studytime'
dependant_variable="G3"

style.use('ggplot')
pyplot.scatter(data[independant_variable],data[dependant_variable])

pyplot.xlabel('independant_variable variable: {}'.format(independant_variable))
pyplot.ylabel('dependant variable / value we are trying to predict: {}'.format(dependant_variable))
pyplot.show()
pyplot.close()
