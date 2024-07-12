# import streamlit as st
# import pickle
# import pandas as pd

# with open('svc_pipeline_optimized.pkl', 'rb') as file:
#     svc_pipeline_optimized = pickle.load(file)

# st.title('Stroke Prediction')

# age = st.number_input('Enter Age', min_value=0, max_value=120, value=25)

# if st.button('Predict'):
   
#     input_data = pd.DataFrame({'Age': [age]})
    
#     prediction = svc_pipeline_optimized.predict(input_data)
    
#     stroke_result = 'YES' if prediction[0] == 1 else 'NO'
#     st.write(f'Stroke: {stroke_result}')




import streamlit as st
import pickle
import pandas as pd

# Load the optimized SVC pipeline model
with open('svc_pipeline_optimized.pkl', 'rb') as file:
    svc_pipeline_optimized = pickle.load(file)

# Streamlit app title
st.title('Stroke Prediction')

# Input fields for Age, Hypertension, Heart Disease, and AVG Glucose
age = st.number_input('Enter Age', min_value=0, max_value=120, value=25)
hypertension = st.selectbox('Hypertension', [0, 1])
heart_disease = st.selectbox('Heart Disease', [0, 1])
avg_glucose = st.number_input('AVG Glucose', min_value=55, max_value=300, value=100)

# Predict button
if st.button('Predict'):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'Age': [age],
        'Hypertension': [hypertension],
        'Heart_Disease': [heart_disease],
        'AVG_Glucose': [avg_glucose]
    })
    
    # Make prediction using the loaded model
    prediction = svc_pipeline_optimized.predict(input_data)
    
    # Display prediction result
    stroke_result = 'YES' if prediction[0] == 1 else 'NO'
    st.write(f'Stroke: {stroke_result}')
   
