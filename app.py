import streamlit as st
from styles import inject_custom_css
from components.health_form import get_user_health_inputs
from components.ingredient_input import get_selected_ingredients
from components.recipe_results import show_matched_recipes

inject_custom_css()

st.image("https://img.freepik.com/free-photo/top-view-vegan-salad-with-lettuce_23-2148723457.jpg", use_column_width=True)
st.title("🥗 Nutrilyze+")
st.markdown("### *Delicious recipes tailored to your health, mood, and kitchen!*")

health_condition, taste_preference = get_user_health_inputs()
st.markdown("---")
selected_ingredients = get_selected_ingredients()
st.markdown("---")

if st.button("🔍 Show Recipes"):
    show_matched_recipes(health_condition, taste_preference, selected_ingredients)


