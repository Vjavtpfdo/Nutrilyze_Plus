import streamlit as st

def get_user_health_inputs():
    st.header("🩺 Your Health & Taste Preferences")

    condition = st.selectbox("Select your health condition:", [
        "None", "Diabetes", "Hypertension", "PCOS", "Obesity", "Cholesterol",
        "Vitamin Deficiency", "Cold", "Anti-inflammatory", "Energy Boost", "Easy Digest"
    ])
    
    taste = st.radio("Choose your preferred taste:", ["Savory", "Spicy", "Sweet", "Tangy", "No Preference"])

    return condition, taste
