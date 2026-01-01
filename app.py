import streamlit as st
import joblib
import numpy as np

model = joblib.load("mental_health_model.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Mental Health Companion")
st.title("Mental Health Companion Chatbot")

st.write(
    "I will ask you a few questions to understand how you’re feeling.\n"
    "**Answer on a scale of 1 to 5** (1 = very low, 5 = very high).\n\n"
    "*This is not a medical diagnosis.*"
)

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

questions = {
    "sleep": "How has your sleep been recently?",
    "appetite": "How is your appetite?",
    "interest": "Do you feel interested in daily activities?",
    "fatigue": "Do you feel tired most of the day?",
    "worthlessness": "Do you feel worthless or guilty?",
    "concentration": "Are you able to concentrate properly?",
    "agitation": "Do you feel restless or agitated?",
    "suicidal_ideation": "Do you experience harmful thoughts?",
    "sleep_disturbance": "Do you wake up frequently at night?",
    "aggression": "Do you feel irritable or angry?",
    "panic_attacks": "Do you experience panic or anxiety?",
    "hopelessness": "Do you feel hopeless about the future?",
    "restlessness": "Do you find it hard to stay calm?",
    "low_energy": "Do you feel low energy most of the time?"
}
if st.session_state.step < len(features):
    feature = features[st.session_state.step]
    st.write(f"**Bot:** {questions[feature]}")

    user_input = st.text_input("Your answer (1-5):", key=feature)

    if st.button("Next"):
        if user_input.isdigit() and 1 <= int(user_input) <= 5:
            st.session_state.answers.append(int(user_input))
            st.session_state.step += 1
            st.experimental_rerun()
        else:
            st.warning("Please enter a number between 1 and 5.")

else:
    user_array = np.array([st.session_state.answers])
    prediction = model.predict(user_array)[0]

    st.subheader("Chatbot Response")

    if prediction == 0:
        st.success("You seem emotionally stable. Keep taking care of yourself.")
        st.write("Tip: Maintain good sleep, balanced meals, and regular breaks.")
    else:
        st.warning("💙 You may be experiencing emotional distress.")
        st.write(
            "You are not alone.\n\n"
            "Try slow breathing, journaling, or talking to someone you trust.\n"
            "If these feelings persist, please consider professional support."
        )

    if st.button("Restart Chat"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.experimental_rerun()
