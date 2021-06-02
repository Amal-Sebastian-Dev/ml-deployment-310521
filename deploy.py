#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 

st.title('Student Indicator Dataset - 2014')

st.set_option('deprecation.showPyplotGlobalUse', False)

#import dataset
df = pd.read_csv('edu_indicators_14.csv')

# Display the first 10 rows of the table
edu_data = df.head()
st.table(edu_data)

# Average EPE
avg_epe = df.EPE.mean()
st.text('Average enrollment in primary education {}'.format(avg_epe))

# Minimum UNEMP
min_unemployment = df.min()
st.text('{} has minimum unemployment.({})'.format(min_unemployment['Country Name'], min_unemployment.UNEMP))

# plots
st.subheader('Relation between Population, GDP, Secondary Education Enrollment and Unemployment')
sns.pairplot(df, vars=['PPT', 'GDP', 'ESE', 'UNEMP'], palette='rainbow', kind='reg')
st.pyplot()
