import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout='wide',
                   page_icon="👩‍⚕️")

# Load pre-trained models
diabetes_model = pickle.load(open(r"C:\Users\bhagy\OneDrive\Desktop\predict internship\training_models\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\bhagy\OneDrive\Desktop\predict internship\training_models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\bhagy\OneDrive\Desktop\predict internship\training_models\parkinsons_model.sav", 'rb'))

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson’s Prediction'], 
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction
if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the person")
    
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction
# Heart Disease Prediction
elif selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        ChestPain = st.text_input('Chest Pain Type (0-3)')
    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')
    with col2:
        Cholesterol = st.text_input('Cholesterol Level')
    with col3:
        FastingBS = st.text_input('Fasting Blood Sugar (1 = True, 0 = False)')
    with col1:
        RestECG = st.text_input('Resting Electrocardiographic Results (0-2)')
    with col2:
        MaxHR = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        ExerciseAngina = st.text_input('Exercise-Induced Angina (1 = Yes, 0 = No)')
    with col1:
        Oldpeak = st.text_input('Old Peak')
    with col2:
        Slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        CA = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        Thal = st.text_input('Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)')
    
    if st.button('Heart Disease Test Result'):
        # Ensure all 13 features are collected
        user_input = [
            float(Age), float(Sex), float(ChestPain), float(RestingBP), float(Cholesterol),
            float(FastingBS), float(RestECG), float(MaxHR), float(ExerciseAngina), 
            float(Oldpeak), float(Slope), float(CA), float(Thal)
        ]
        
        # Make prediction
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
        st.success(heart_diagnosis)


# Parkinson's Disease Prediction
elif selected == "Parkinson’s Prediction":
    st.title('Parkinson’s Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo (Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi (Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo (Hz)')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter (%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shim = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shim_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        Spread1 = st.text_input('Spread1')
    with col2:
        Spread2 = st.text_input('Spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
    
    if st.button('Parkinsons Disease Test Result'):
        user_input = [float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo), float(MDVP_Jitter_percent),
                          float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                          float(MDVP_Shim), float(MDVP_Shim_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                          float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE), 
                          float(DFA), float(Spread1), float(Spread2), float(D2), float(PPE)]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinsons disease' 
        else: 
            parkinsons_diagnosis='The person does not have Parkinsons disease'
        st.success(parkinsons_diagnosis)