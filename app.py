import streamlit as st
import joblib
import pandas as pd
import sys, os, streamlit as st
st.write("sys.argv:", sys.argv)
st.write("STREAMLIT_SERVER_RUNNING:", os.environ.get("STREAMLIT_SERVER_RUNNING"))


#st.write("Hello World!")
#st.title("Time Estimation Model")
st.set_page_config(
    page_title="Delivery Time Estimator",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .big-header {
        font-size:32px;
        font-weight:700;
    }
    .card {
        background: linear-gradient(180deg, #ffffff 0%, #f7fafc 100%);
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
    }
    .metric-big {
        font-size: 34px;
        font-weight: 700;
    }
    .muted {
        color: #6b7280;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

distance_km = st.number_input("Enter Distance in KM: ", min_value=1, value=1, step=1)

weather = st.selectbox("Choose weather type", ['Clear', 'Rainy', 'Foggy', 'Snowy', 'Windy'], key='weather_type', index=0)

traffic = st.selectbox("Choose traffic type", ['Medium', 'Low', 'High'], key='traffic_type', index=2)

time_of_day = st.selectbox("Choose Time of Day", ['Morning', 'Evening', 'Afternoon','Night'], key='time_of_day', index=1)

vehicle_type = st.selectbox("Choose Vehicle Type", ['Bike', 'Scooter', 'Car'], key='vehicel_type', index=0)

preparation_time = st.number_input("Enter preparation time in minutes:", min_value=1, value=1, step=1)

experience_yrs = st.number_input("Enter Courier boy experience in years: ", min_value=1, value=1, step=1)

# Model import

model = joblib.load("Time_Estimation_Model.pkl")

input_data = pd.DataFrame({
        "Distance_km": [distance_km],
        "Weather": [weather],
        "Traffic_Level": [traffic],
        "Time_of_Day": [time_of_day],
        "Vehicle_Type": [vehicle_type],
        "Preparation_Time_min": [preparation_time],
        "Courier_Experience_yrs": [experience_yrs],
        })

if st.button('Predict'):
    #columns = ['Distance_km', 'Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type', 'Preparation_Time_min', 'Courier_Experience_yr']
    prediction = model.predict(input_data)
    st.success(f"⏱️ Estimated Delivery Time: **{prediction[0]:.2f} minutes**")