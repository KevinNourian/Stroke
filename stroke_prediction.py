import streamlit as st
import pickle
import pandas as pd

with open('svc_pipeline_optimized.pkl', 'rb') as file:
    svc_pipeline_optimized = pickle.load(file)

st.title('Stroke Prediction')

age = st.number_input('Enter Age', min_value=0, max_value=120, value=25)

if st.button('Predict'):
   
    input_data = pd.DataFrame({'Age': [age]})
    
    prediction = svc_pipeline_optimized.predict(input_data)
    
    stroke_result = 'YES' if prediction[0] == 1 else 'NO'
    st.write(f'Stroke: {stroke_result}')
