import streamlit as st
import joblib
import numpy as np

model = joblib.load("mental_health_model.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Mental Health Companion")
st.title("Mental Health Companion Chatbot")

st.write(
    "I will ask you a few questions to understand how you’re feeling.\n"
    "\n**Answer on a scale of 1 to 5** (1 = very low, 5 = very high).\n\n"
    "*This is not a medical diagnosis.*"
)

if "welcomed" not in st.session_state:
    st.session_state.chat_history = [{
        "role": "bot",
        "message": "Hi I’m here to listen."
    }]
    st.session_state.welcomed = True

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

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

progress = st.session_state.step / len(features)
st.progress(progress)
st.caption(f"Question {st.session_state.step + 1} of {len(features)}")


for chat in st.session_state.chat_history:
    role_icon = "Bot" if chat["role"] == "bot" else "You"
    st.markdown(f"**{role_icon}:** {chat['message']}")

if st.session_state.step < len(features):
    feature = features[st.session_state.step]
    bot_question = questions[feature]

    if st.session_state.chat_history[-1]["message"] != bot_question:
        st.session_state.chat_history.append(
            {"role": "bot", "message": bot_question}
        )
        st.rerun()

    user_input = st.text_input(
        "Your answer (1–5):",
        key=f"input_{st.session_state.step}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Send"):
            if user_input.isdigit() and 1 <= int(user_input) <= 5:
                st.session_state.chat_history.append(
                    {"role": "user", "message": user_input}
                )
                st.session_state.answers.append(int(user_input))
                st.session_state.step += 1
                st.rerun()
            else:
                st.warning("Please enter a number between 1 and 5.")

    with col2:
        if st.button("Edit Previous Answer") and st.session_state.step > 0:
            st.session_state.chat_history.pop()
            st.session_state.chat_history.pop()
            st.session_state.answers.pop()
            st.session_state.step -= 1
            st.rerun()

else:
    user_array = np.array([st.session_state.answers])
    prediction = model.predict(user_array)[0]

    probability = model.predict_proba(user_array)[0][1] * 100

    st.subheader("Chatbot Response")
    st.caption(f"Emotional distress likelihood: {probability:.1f}%")

    if prediction == 0:
        st.success(
            "You seem emotionally stable.\n\n"
            "💡 Maintain healthy sleep, balanced meals, and regular breaks."
        )
    else:
        st.warning(
            "You may be experiencing emotional distress.\n\n"
            "- Try deep breathing or mindfulness\n"
            "- Talk to a trusted friend or family member\n"
            "- Maintain a simple daily routine"
        )
        st.info(
            "If you ever feel unsafe or overwhelmed, please reach out to:\n\n"
            "- A trusted person\n"
            "- A licensed mental health professional\n"
            "- A local mental health helpline"
        )

    if st.button("Restart Chat"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.session_state.chat_history = [{
            "role": "bot",
            "message": "Hi I’m here to listen."
        }]
        st.rerun()

st.markdown(
    "<hr><center>Made for student mental well-being</center>",
    unsafe_allow_html=True
)
