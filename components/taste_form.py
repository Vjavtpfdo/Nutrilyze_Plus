# components/taste_form.py
import streamlit as st

def taste_form(condition: str | None) -> str:
    tastes = {
        "Diabetes": ["No Preference", "Bitter", "Astringent", "Sour", "Salty","Spicy"],
        "High Cholesterol": ["No Preference", "Bitter", "Astringent","Sour","Spicy"],
        "Eye Health": ["No Preference", "Bitter", "Astringent", "Sweet", "Salty","Spicy"],
        "Hypothyroidism": ["No Preference", "Spicy","Astringent","Bitter","Savory",]
    }
    st.subheader("😋 Select Your Taste Preference")
    return st.radio("Choose your taste preference:", tastes.get(condition, ["No Preference"]), key="taste_radio")
