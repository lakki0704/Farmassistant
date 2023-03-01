import numpy as np # linear algebra
import pandas as pd
import pickle

df=pd.read_csv("Crop_recommendation.csv")

from sklearn import preprocessing

from sklearn.metrics import classification_report
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyClassifier

#Data Pre-Processing
from sklearn.preprocessing import LabelEncoder
X = df.drop('label' ,axis =1)
y = df['label']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1, random_state=42)

#rice = 1 , maize = 2 , chickpea -3 ,kidneybeans -4 , pigeonpeas -5, mothbeans -6 , mungbean -7, blackgram -8
#lentil -9 , pomegrenate =10 , banana =11, mango -12 , grapes -13 ,watermelon -14  , muskmelon -15, apple -16
#orange - 17, papaya -18 ,coconut -19 ,cotton -20, jute -21,coffee-22,

#Decision Tree
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(X_train , y_train)

pickle.dump(DT, open('model.pkl','wb'))

input = [28,74,81,18.01272266,18.30968112,8.753795334,81.98568791]
input = np.array(input).reshape(1,-1);
predict = DT.predict(input)

if(predict==3):
    print("Chickpea")


