import streamlit as st
import tensorflow as tf
import joblib
import numpy as np

st.title('Graduate Admission Chance Predictor')

# Load the trained model and scaler
model = tf.keras.models.load_model('C:/Users/HP/Downloads/graduate_admission/keras_model.keras')
scaler = joblib.load('C:/Users/HP/Downloads/graduate_admission/minmax_scaler.pkl')

st.write("Model and scaler loaded successfully!")

st.header('Enter Student Details:')

# Create input fields for the features
gre_score = st.slider('GRE Score', 290, 340, 315)
toefl_score = st.slider('TOEFL Score', 90, 120, 105)
university_rating = st.slider('University Rating', 1, 5, 3)
sop = st.slider('SOP (Statement of Purpose) Score', 1.0, 5.0, 3.0, 0.5)
lor = st.slider('LOR (Letter of Recommendation) Score', 1.0, 5.0, 3.0, 0.5)
cgpa = st.slider('CGPA (Cumulative Grade Point Average)', 6.5, 10.0, 8.0, 0.01)
research = st.selectbox('Research Experience (1=Yes, 0=No)', options=[0, 1])


if st.button('Predict Chance of Admit'):
    # Combine all inputs into a numpy array
    input_data = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])

    # Scale the input data
    scaled_input_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_input_data)[0][0]

    st.subheader('Prediction:')
    st.write(f'Predicted Chance of Admit: {prediction:.2f}')
