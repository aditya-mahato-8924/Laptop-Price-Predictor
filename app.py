import streamlit as st
import requests
from config.categories import *

# set the title
st.markdown(
    "<h1 style='text-align: center;'>Laptop Price Predictor</h1>",
    unsafe_allow_html=True
)
st.markdown('Enter the details below:')

# api url
API_URL = 'https://laptop-price-predictor-api-j6m8.onrender.com/predict'


col1, col2, col3, col4 = st.columns(4)

with col1:
    Company = st.selectbox('Company', options=COMPANIES)
    TypeName = st.selectbox('Laptop Type', options=LAPTOP_TYPES)
    Ram = st.number_input('RAM (in GB)', min_value=2, value=8)
    Weight = st.number_input('Weight (in Kg)', min_value=0.8, value=1.8)
    GPU_brand = st.selectbox('GPU Brand', options=GPU_BRANDS)

with col2:
    Touchscreen = st.selectbox('Touchscreen', options=[0, 1])
    IPSpanel = st.selectbox('IPS Panel', options=[0, 1])
    PPI = st.number_input('PPI', min_value=90.0, value=160.2)
    RetinaDisplay = st.selectbox('Retina Display', options=[0, 1])

with col3:
    CPU_freq = st.number_input('CPU Frequency (in GHz)', min_value=0.8, value=1.3)
    CPU_brand = st.selectbox('CPU Brand', options=CPU_BRANDS)

    if CPU_brand == 'Intel':
        Processor = st.selectbox('Processor', options=PROCESSORS_INTEL)
    else:
        Processor = st.selectbox('Processor', options=PROCESSORS_AMD)
    
    if Company == 'Apple':
        OS = st.selectbox('Operating System', options=['Mac'])
    else:
        OS = st.selectbox('Operating System', options=OS_OPTIONS)

with col4:
    PrimaryStorageType = st.selectbox('Primary Storage Type', options=PRIMARY_STORAGE_TYPE)
    SecondaryStorageType = st.selectbox('Secondary Storage Type', options=SECONDARY_STORAGE_TYPE)
    PrimaryStorage = st.number_input('Primary Storage Capacity (in GB)', min_value=16.0, value=512.0)
    if SecondaryStorageType == 'No':
        SecondaryStorage = st.number_input('Secondary Storage Capacity (in GB)', min_value=0.0, max_value=0.0, value=0.0)
    else:
        SecondaryStorage = st.number_input('Secondary Storage Capacity (in GB)', min_value=8.0, value=128.0)

# predict the price
if st.button('Predict'):
    input_data = {
        'Company':  Company,
        'TypeName': TypeName,
        'Ram': Ram,
        'Weight': Weight,
        'Touchscreen': Touchscreen,
        'IPSpanel': IPSpanel,
        'PPI': PPI,
        'RetinaDisplay': RetinaDisplay,
        'CPU_freq': CPU_freq,
        'CPU_brand': CPU_brand,
        'Processor': Processor,
        'OS': OS,
        'GPU_brand': GPU_brand,
        'PrimaryStorage': PrimaryStorage,
        'SecondaryStorage': SecondaryStorage,
        'PrimaryStorageType': PrimaryStorageType,
        'SecondaryStorageType': SecondaryStorageType
    }

    # pass the data to the api
    try:
        response = requests.post(API_URL, json=input_data)
        prediction = response.json()

        if response.status_code == 200:
            predicted_price = prediction['predicted_price']
            
            # display the result on the web app
            st.success(
                f"Based on the selected configuration, the predicted price is "
                f"₹{predicted_price:,.0f}. "
            )
        else:
            # return the error
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f'Could not connect with the FastAPI server: {e}, \nTry again some other time')