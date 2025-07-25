import streamlit as st

def get_selected_ingredients():
    st.header("🛒 Ingredients You Have at Home")
    st.markdown("*Note: Salt and Sugar are taken as default ingredients.*")

    categories = {
        "Vegetables": ["ash gourd", "beans", "bitter gourd", "cabbage", "carrot", "drumstick leaves", "onion", "potato", "spinach", "tomato", "coriander", "mint", "neem flower", "pumpkin"],
        "Fruits": ["banana", "pomegranate", "lemon"],
        "Dairy": ["milk", "curd", "paneer"],
        "Grains & Pulses": ["rice", "wheat", "oats", "ragi", "semolina", "moong dal", "toor dal", "urad dal", "masoor dal", "broken wheat"],
        "Spices & Seasonings": ["turmeric", "pepper", "cumin", "mustard seeds", "cardamom", "garlic", "ginger", "green chili", "black pepper", "chili", "tamarind"],
        "Others": ["egg", "bread", "bread crumbs", "ghee", "jaggery", "sugar", "honey", "salt", "oil", "curry leaves", "chia seeds"]
    }

    all_selected = []
    for cat, items in categories.items():
        with st.expander(cat):
            selected = st.multiselect(f"Select from {cat}:", items)
            all_selected.extend([s.lower() for s in selected])

    # Add salt and sugar as default
    all_selected.extend(["salt", "sugar"])
    return all_selected
