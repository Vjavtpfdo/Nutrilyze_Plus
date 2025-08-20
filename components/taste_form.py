#components/taste_form.py
import streamlit as st

def get_taste_preference():
    return st.radio(
        "Choose your preferred taste:",
        ["Savory", "Spicy", "Sweet", "Tangy", "No Preference"],
        horizontal=False
    )
