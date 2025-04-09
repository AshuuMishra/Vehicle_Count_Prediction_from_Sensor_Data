
import streamlit as st
import pickle
import numpy as np

# Load the trained model (you'll need to save it first!)
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("🚗 Vehicle Count Prediction App")
st.write("Enter the details below to predict the number of vehicles:")

# Input fields
date = st.number_input("Date (day of month)", min_value=1, max_value=31, value=1)
weekday = st.number_input("Weekday (0 = Monday, 6 = Sunday)", min_value=0, max_value=6, value=0)
hour = st.number_input("Hour of the day (0-23)", min_value=0, max_value=23, value=0)
month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=1)
year = st.number_input("Year (e.g., 2015)", min_value=2000, max_value=2100, value=2015)
dayofyear = st.number_input("Day of Year (1-366)", min_value=1, max_value=366, value=1)
weekofyear = st.number_input("Week of Year (1-52)", min_value=1, max_value=52, value=1)

# Prediction button
if st.button("Predict Vehicle Count"):
    # Prepare input
    input_data = np.array([[date, weekday, hour, month, year, dayofyear, weekofyear]])
    prediction = model.predict(input_data)
    
    # Show result
    st.success(f"Estimated number of vehicles: {int(prediction[0])}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 