import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
import matplotlib
matplotlib.rcParams["figure.figsize"]=(20,10)
df1=pd.read_csv("C:\\Users\\Anushka\\Desktop\\IndividualDetailsofCoronaAffectants.csv")
df1.fillna(0,inplace=True)
df1.shape
df2=df1.drop(['ID','Unique id','Government id','Gender','Detected city pt','Nationality','Current location','Current location pt','Created on','Updated on','Contacts'],axis='columns')
df2.isnull().sum()
df2['Detected state'].unique()
df2=df2.drop(['Status change date'],axis='columns')
df2['Current status'].unique()
