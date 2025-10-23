# app.py
import streamlit as st
from auth_component import auth_page
from auth_utils import init_db
from styles import inject_custom_css

from components.health_form import get_user_health_inputs
from components.taste_form import taste_form
from components.ingredient_input import get_selected_ingredients
from components.recipe_results import show_matched_recipes

init_db()
inject_custom_css()

if "page" not in st.session_state:
    st.session_state.page = "auth"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.page == "auth":
    auth_page()
    if st.session_state.get("authenticated", False):
        st.session_state.page = "health"
        st.rerun()

elif st.session_state.page == "health":
    st.markdown("## 🌟 Welcome — Choose a health condition to continue")
    condition = get_user_health_inputs()
    if st.session_state.get("health_condition"):
        st.session_state.page = "taste_ingredient"
        st.rerun()

elif st.session_state.page == "taste_ingredient":
    st.markdown("## 🍽 Customize Your Preferences")
    condition = st.session_state.get("health_condition", None)
    if not condition:
        st.warning("No health condition selected. Returning to Health selection.")
        st.session_state.page = "health"
        st.rerun()

    taste_pref = taste_form(condition)
    st.session_state.taste_preference = taste_pref
    ingredients = get_selected_ingredients(condition)
    st.session_state.ingredients = ingredients

    if st.button("Show Recipes 🍲", use_container_width=True, key="show_recipes"):
        st.session_state.page = "results"
        st.rerun()

    st.markdown("---")
    if st.button("🔙 Back to Health Selection", key="back_to_health"):
        st.session_state.pop("taste_preference", None)
        st.session_state.pop("ingredients", None)
        st.session_state.pop("health_condition", None)
        st.session_state.page = "health"
        st.rerun()

elif st.session_state.page == "results":
    st.markdown("## 🍲 Recommended Recipes")
    show_matched_recipes(
        st.session_state.get("health_condition"),
        st.session_state.get("taste_preference"),
        st.session_state.get("ingredients", []),
    )
    if st.button("🔙 Back to Preferences"):
        st.session_state.page = "taste_ingredient"
        st.rerun()