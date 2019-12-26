# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:13:27 2019

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
 

dataset=pd.read_excel('Data.xlsx')

X = dataset.iloc[:, :-1]


y = dataset.iloc[:,-1]

X.Gender.unique() #One Method for getting the unique Values 

X.Occupation.unique()

X['Phone Type'].unique()    #Another Method for getting the unique Values 


X['Current Bike'].unique()

X['Relationship'].unique()

y.unique()

def Gender_to_int(word):
    word_dict = {'Male ':2, 'Female':1}
    return word_dict[word]

def Occupation_to_int(word):
    word_dict = {'Professional':3, 'Self Employed':2, 'Unemployed':1, 'Student':4}
    return word_dict[word]

def PhoneType_to_int(word):
    word_dict = {'Average':2, 'Low End':1, 'High End':3}
    return word_dict[word]

def CurrentBike_to_int(word):
    word_dict = {'180 to 220':4, 'No Bike':1, '220 and Above':5, '125 to 180':3, 'Below 125':2}
    return word_dict[word]

def Relationship_to_int(word):
    word_dict = {'Complicated':3, 'Single':2, 'Married':1, 'Committed':4}
    return word_dict[word]

def Response_to_int(word):
    word_dict = {'Not purchased':0, 'Purchased':1}
    return word_dict[word]

X['Gender'] = X['Gender'].apply(lambda x : Gender_to_int(x))

X['Occupation'] = X['Occupation'].apply(lambda x : Occupation_to_int(x))

X['Phone Type'] = X['Phone Type'].apply(lambda x : PhoneType_to_int(x))

X['Current Bike'] = X['Current Bike'].apply(lambda x : CurrentBike_to_int(x))

X['Relationship'] = X['Relationship'].apply(lambda x : Relationship_to_int(x))

y = y.apply(lambda x : Response_to_int(x))

#X.info()
 
from sklearn.linear_model import LogisticRegression  
classifier = LogisticRegression()
classifier.fit(X, y)

pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print((model.predict_proba([[23,2,3,2,4,3]])*100).tolist()[0][1])
