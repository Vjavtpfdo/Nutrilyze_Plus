# components/ingredient_input.py
import streamlit as st

def get_selected_ingredients():
    st.header("🛒 Ingredients You Have at Home")
    st.markdown("*Note: Salt and Sugar are taken as default ingredients.*")

    categories = {
        "Vegetables": ["ash gourd", "beans", "bitter gourd", "cabbage", "carrot",
                       "drumstick leaves", "onion", "potato", "spinach", "tomato",
                       "coriander", "mint", "neem flower", "pumpkin"],
        "Fruits": ["banana", "pomegranate", "lemon"],
        "Dairy": ["milk", "curd", "paneer"],
        "Grains & Pulses": ["rice", "wheat", "oats", "ragi", "semolina",
                            "moong dal", "toor dal", "urad dal", "masoor dal", "broken wheat"],
        "Spices & Seasonings": ["turmeric", "pepper", "cumin", "mustard seeds",
                                "cardamom", "garlic", "ginger", "green chili", "black pepper",
                                "chili", "tamarind"],
        "Others": ["egg", "bread", "bread crumbs", "ghee", "jaggery", "honey",
                   "salt", "oil", "curry leaves", "chia seeds"]
    }

    all_selected = []
    for cat, items in categories.items():
        with st.expander(cat, expanded=(cat == "Vegetables")):
            chosen = st.multiselect(f"Select from {cat}:", items, key=f"{cat}_ms")
            all_selected.extend(chosen)

    # salt & sugar default assumption
    if "salt" not in [x.lower() for x in all_selected]:
        all_selected.append("salt")

    return all_selected
