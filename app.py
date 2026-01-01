
import streamlit as st
import joblib
import numpy as np

model = joblib.load("mental_health_model.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Mental Health Companion Chatbot")
st.title("Mental Health Companion Chatbot")
st.write("""
Students often face stress, anxiety, and loneliness but hesitate to approach professional counselors.  
This AI-driven chatbot helps detect emotional distress and provides **supportive responses and relaxation tips**.  
**Disclaimer:** This chatbot does not diagnose mental health conditions.
""")
st.header("Answer the following questions (1 = low, 5 = high)")

user_data = []

for feature in features:
    value = st.slider(f"{feature.replace('_', ' ').title()}", 1, 5)
    user_data.append(value)


sleep = st.slider("How has your sleep been lately?", 1, 5)
appetite = st.slider("How is your appetite?", 1, 5)
interest = st.slider("Are you interested in daily activities?", 1, 5)
fatigue = st.slider("How tired do you feel during the day?", 1, 5)
concentration = st.slider("How well can you concentrate?", 1, 5)
low_energy = st.slider("Do you feel low energy most of the time?", 1, 5)
hopelessness = st.slider("Do you feel hopeless at times?", 1, 5)
panic_attacks = st.slider("Do you experience panic or anxiety?", 1, 5)


if st.button("Check My Emotional Well-being"):

    user_input = np.array([[sleep, appetite, interest, fatigue, concentration, low_energy, hopelessness, panic_attacks]])
    

    prediction = model.predict(user_input)[0]

    if prediction == 0:
        st.success("You seem emotionally stable. Keep taking care of yourself!")
        st.info("Tip: Maintain healthy sleep, balanced meals, and stay active.")
    else:
        st.warning("You may be experiencing emotional distress. You're not alone.")
        st.info("""
        Here are some tips that may help:  
        - Talk to a trusted friend, family member, or counselor  
        - Try deep breathing or mindfulness exercises  
        - Take short breaks and engage in a relaxing activity  
        - Maintain a routine and healthy sleep schedule
        """)

