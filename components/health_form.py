#components/health_form.py
import streamlit as st

def get_user_health_inputs():
    st.subheader("💊 Select Your Health Condition")
    st.write("This will help us recommend recipes suited to your health needs.")

    health_condition = st.selectbox(
        "Choose your current health condition:",
        ["None", "PCOS", "Hypertension", "Cold", "Diabetes", "Acidity",
         "Thyroid Issues", "Weight Loss", "High Cholesterol"]
    )

    st.subheader("😋 Choose Your Taste Preference")
    taste_preference = st.selectbox(
        "What type of taste do you prefer?",
        ["Any", "Spicy", "Savory", "Sweet", "Tangy"]
    )

    return health_condition, taste_preference
