#Define all the Libraries. The model libraries have not been added here
import streamlit as st
import pandas as pd


#Define all the Sections
header = st.container()
Loaddata = st.container()


#@st.cache
def good_data():
	#Place the Raw data (Raw.txt) in the location
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Good_Residential.csv')
def bad_data():
	#Place the pre-processed data (Final_Usage.csv) in the location
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Final_Bad_Resident.csv')


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
		





	
	
