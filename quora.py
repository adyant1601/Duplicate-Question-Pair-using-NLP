# streamlit_app.py

import requests
import streamlit as st
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings (because using ngrok etc.)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Streamlit app UI
st.title("Duplicate Question Classifier")

q1 = st.text_input("Enter Question 1:")
q2 = st.text_input("Enter Question 2:")

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

# Replace below URL with your ngrok URL
backend_url = "http://0844-35-199-186-18.ngrok-free.app/predict"

if st.button("Check Duplicate"):
    if q1 and q2:
        session = requests.Session()
        session.verify = False

        response = session.post(
            backend_url,
            json={'question1': q1, 'question2': q2},
            headers=headers
        )

        try:
            json_response = response.json()
            st.subheader(f"Prediction: {json_response['response']}")
        except ValueError:
            st.error("Error: Response is not JSON format.")
    else:
        st.warning("Please enter both questions.")
