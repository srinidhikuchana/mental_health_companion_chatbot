# Mental Health Companion Chatbot
Students face high levels of stress, anxiety, and loneliness but often hesitate to approach professional counselors. A safe, Al-driven chatbot that detects user mood through sentiment analysis and generates empathetic, motivational responses along with relaxation tips can support student mental well-being.

## Live Overview

The Mental Health Companion Chatbot helps users gain early awareness of their mental health condition by analyzing inputs such as mood, sleep patterns, appetite, fatigue and concentration.
It provides instant predictions in a simple, user-friendly interface.

Note: This tool is for educational and awareness purposes only and does not replace professional medical advice.

## Problem Statement

Mental health disorders like depression often go undetected due to stigma, lack of awareness, and limited access to professionals. Traditional assessment methods can be time-consuming and subjective. This project aims to provide a data-driven, accessible, and fast screening tool to support early mental health awareness.

## Solution Overview

Machine learning model trained on mental health data

Classifies depression severity:

No Depression

Mild

Moderate

Severe

Interactive Streamlit frontend for real-time predictions

Lightweight and easy to deploy

## Tech Stack

Language: Python

Frontend: Streamlit

ML Libraries: scikit-learn, Pandas, NumPy

Model Storage: Pickle (.pkl)

Development: Jupyter Notebook / Google Colab

## Project Structure
mental_health_companion_chatbot/
│

├── mental_health.csv          
├── model_training.ipynb       
├── mental_health_model.pkl    
├── features.pkl               
├── app.py                     
├── README.md                  
├── requirements.txt           


## How to Download & Run
1.  Download the Project

Click Code → Download ZIP on GitHub
or clone the repository:

git clone <repository-link>
cd mental_health_companion_chatbot

2️. Install Dependencies
pip install -r requirements.txt

3️. Run the Application
streamlit run app.py


The app will open automatically in your browser.

## How It Works

User enters mental health indicators through the Streamlit UI

Data is processed and passed to the trained ML model

The system predicts depression severity instantly

Results are displayed in a clear and understandable format

## Future Enhancements
Wearable device integration (sleep, stress, activity data)

Real-time mental health monitoring

Conversational AI for emotional support

Multimodal analysis (text, voice, facial expressions)

Stronger privacy and ethical AI safeguards

## Conclusion
This project demonstrates how AI and machine learning can support early mental health awareness through accessible and interactive technology. The Mental Health Companion Chatbot serves as a foundation for building more advanced, intelligent mental health support systems.

## Disclaimer
This project is intended for educational and research purposes only and should not be used as a substitute for professional mental health diagnosis or treatment.
