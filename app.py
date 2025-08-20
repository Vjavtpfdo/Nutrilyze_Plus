#app.py
import streamlit as st

from styles import inject_custom_css
from auth_component import auth_page
from components.health_form import get_user_health_inputs
from components.ingredient_input import get_selected_ingredients
from components.recipe_results import show_matched_recipes

# ---- Page config FIRST ----
st.set_page_config(page_title="Nutrilyze+", page_icon="🥗", layout="centered")

# ---- Global styles ----
inject_custom_css()

# ---- Auth gate ----
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    auth_page()
    st.stop()   # do not render the rest until authenticated

# ---- App content (after login) ----
with st.container():
    st.title("🥗 Nutrilyze+")
    st.markdown("### *Delicious recipes tailored to your health, mood, and kitchen!*")
    st.markdown("---")

    # Health and taste inputs
    health_condition, taste_preference = get_user_health_inputs()

    st.markdown("---")

    # Ingredient selection
    selected_ingredients = get_selected_ingredients()

    st.markdown("---")

    if st.button("🔍 Show Recipes"):
        show_matched_recipes(health_condition, taste_preference, selected_ingredients)
