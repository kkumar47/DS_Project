#Define all the Libraries. The model libraries have not been added here
import streamlit as st
import dask.dataframe as dd
import pandas as pd
import numpy as np
import datetime as dt
import calendar
import random
#from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Activation, Flatten,  BatchNormalization, Conv1D,MaxPooling1D
from tensorflow.keras.models import Sequential
#from tensorflow.keras import layers
#from tensorflow.keras import regularizers
#from tensorflow.keras.utils import plot_model

#from sklearn.ensemble import RandomForestClassifier

#Define all the Sections
header = st.container()
Loaddata = st.container()
preprocess = st.container()

#@st.cache
def good_data():
	#Place the Raw data (Raw.txt) in the location
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Good_Residential.csv')
def bad_data():
	#Place the pre-processed data (Final_Usage.csv) in the location
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Final_Bad_Resident.csv')
def condition(x):
  if (x=='August' or x=='September' or x=='October'):
    return "Autumn"
  elif (x=='November' or x=='December' or x=='January'):
    return "Winter"
  elif (x=='February' or x=='March' or x=='April'):
    return "Spring"
  elif (x=='May' or x=='June' or x=='July'):
    return "Summer"
def pprocess():
	Good_Residential = good_data()
	Good_Residential = Good_Residential.head(1000)
	Good_Residential = Good_Residential[['Meter', 'Date_Raw','Usage']]
	Good_Residential['Hr'] = (((Good_Residential['Date_Raw']-1)%100)*30)//60
	Good_Residential['Day'] = abs(Good_Residential['Date_Raw']//100)
	Good_Residential = Good_Residential.drop(columns=['Date_Raw'])
	Good_Residential['Date'] = Good_Residential['Day'].apply(lambda x: pd.to_datetime((2009*1000 )+ x, format = "%Y%j") if x<=365 else pd.to_datetime((2010*1000 )+ (x-365), format = "%Y%j"))
	Good_Residential['Day_Num'] = Good_Residential['Date'].apply(lambda x: x.weekday())
	Good_Residential['Dayname'] = Good_Residential['Date'].apply(lambda x: calendar.day_name[x.weekday()])
	Good_Residential['Holiday_Ind'] = Good_Residential['Day_Num'].apply(lambda x: 0 if x<=4 else 1)
	Good_Residential['Month'] = Good_Residential['Date'].apply(lambda x: x.strftime("%B"))
	Good_Residential['Year'] = Good_Residential['Date'].apply(lambda x: x.year)
	Good_Residential['Season']=Good_Residential['Month'].apply(condition)
	Good_Residential.drop(Good_Residential[Good_Residential['Hr']==24].index, inplace=True)
	st.text('Pre-processed Good Data')
	st.dataframe(Good_Residential.head(10))
	GoodRp= Good_Residential.to_csv().encode('utf-8')
	st.download_button('Download Data', data=GoodRp, file_name='Pre-Processed Good Customer.csv')	

Good_Residential = good_data()
Bad_Residential = bad_data()

with header:
	font="sans serif"
	textColor="#26273"
	st.title('Electricity Theft Prediction')
	
with Loaddata:
	st.subheader("Electricity Usage History data for Customers", anchor ='The Data')
	st.text('Datasource: Electric Ireland and Sustainable Energy Authority of Ireland')
	#The raw data is displayed here
	col1, col2 = st.columns(2)
	with col1:
		st.dataframe(Bad_Residential)
		rawd = Bad_Residential.to_csv().encode('utf-8')
		st.text('Bad Customer Data')
		st.download_button('Download Data', data=rawd, file_name='Bad_Customer_Sample.csv')
	with col2:
		st.dataframe(Good_Residential[['Meter', 'Date_Raw', 'Usage']])
		rawg = Good_Residential.to_csv().encode('utf-8')
		st.text('Good Customer Data')
		st.download_button('Download Data', data=rawd, file_name='Good_Customer_Sample.csv')
		

with preprocess:
	st.subheader("Pre-Process Data")
	st.button('Start Pre-Processing', on_click = pprocess)




	
	
