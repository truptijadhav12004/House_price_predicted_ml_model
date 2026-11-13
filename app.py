
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
import time

from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import MinMaxScaler

st.title('Housing Price Prediction Using Machine Learning')

st.image('https://miro.medium.com/v2/resize:fit:4800/format:webp/0*cDRFtpTiOJFrfzS5.jpg')

st.write('''
We are data enthusiasts passionate about applying machine learning
to real-world problems. Our project Housing Price Prediction
aims to provide accurate and reliable property price estimates.
''')

# Load Dataset
data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

# Select Features
X = df.iloc[:, :-1]

# Load Scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Sidebar Inputs

st.sidebar.title('Select House Features 🏠')

st.sidebar.image(
    'https://cdn-icons-png.flaticon.com/512/619/619153.png',
    width=150
)
all_value = []

for i in X.columns:
    value = st.sidebar.slider(
        f'Select {i} value',
        float(X[i].min()),
        float(X[i].max()),
        float(X[i].mean())
    )
    all_value.append(value)

# Transform Input
final_data = np.array([all_value])
final_data = scaler.transform(final_data)

# Load Model
with open('chatgpt_for_house.pkl', 'rb') as f:
    chatgpt = pickle.load(f)

# Prediction
price = chatgpt.predict(final_data)[0]

if price:
    with st.spinner('Wait for price prediction...'):
        time.sleep(2)

    st.success(
        f'Predicted price is: ${round(price * 100000, 2)}'
    )
