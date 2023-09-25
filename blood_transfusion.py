import streamlit as st
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt

st.title('Blood Transfusion')

# Fetch the CSV file using requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the CSV data into a DataFrame
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))
    # Now you can work with the DataFrame 'df'
else:
    st.error("Failed to retrieve the CSV file.")

st.write("Welcome to our Blood Transfusion app! We will show two interactive visualizations related to the following dataset of which we only show 5 rows:")
st.dataframe(df.head())

st.header("ScatterPlots for Numerical Variables")

st.write("We will start by creating scatterplots using the following four variables:")
st.write("__Recency__: time since the last time a subject intended to donate blood (in months).")
st.write("__Frequency__: total number of blood transfusions per subject.")
st.write("__Monetary__: total quantity of transfused blood (in c.c. blood).")
st.write("__Time__: time since the first time a subject intended to donate blood (in months).")

x_axis = st.selectbox(
    'Start by choosing the x variable',
     df.columns[:4])

y_axis = st.selectbox(
    'Next, choose the y variable',
     df.columns[:4])

plt.figure(figsize=(8, 6))
plt.scatter(df[x_axis], df[y_axis])
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title('Scatter Plot')

st.pyplot(plt)


st.header("Histogram of Varying Bin Size")

st.write("Now, we will plot a histogram of varying bin size of the frequency of the numbers of blood transfusions in subjects.")

s = st.slider('Select Bin Size', min_value=1, max_value=100, value=20)

plt.figure(figsize=(8, 6))
plt.hist(df['Frequency (times)'], bins=s, edgecolor='k')
plt.xlabel('Number of blood transfusions')
plt.ylabel('Frequency of those numbers in subjects')
plt.title(f'Histogram (Bin Size: {s})')

st.pyplot(plt)