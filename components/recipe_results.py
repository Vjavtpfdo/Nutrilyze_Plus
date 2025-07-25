import streamlit as st
from data.load_recipes import load_recipes

recipes = load_recipes()

def show_matched_recipes(health_condition, taste_preference, selected_ingredients):
    matched = []
    
    for recipe in recipes:
        if health_condition != "None" and health_condition not in recipe["health_tags"]:
            continue
        if taste_preference != "No Preference" and taste_preference not in recipe["taste"]:
            continue
        recipe_ing = set(recipe["ingredients"])
        match_ing = recipe_ing.intersection(set(i.lower() for i in selected_ingredients))
        if len(match_ing) / len(recipe_ing) >= 0.75:
            matched.append(recipe)

    if matched:
        st.subheader("🍽️ Recommended Recipes for You:")
        for r in matched:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image("https://source.unsplash.com/400x250/?healthy," + r["name"].split()[0], use_container_width=True)
            with col2:
                st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
                st.markdown(f"<div class='recipe-title'>🍽️ {r['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"**🔥 Calories:** {r['calories']} kcal")
                st.markdown(f"**😋 Taste:** {r['taste']}")
                st.markdown(f"**🩺 Health Tags:** {', '.join(r['health_tags'])}")
                st.markdown(f"**🧂 Ingredients:** {', '.join(r['ingredients'])}")
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.warning("❌ No matching recipes found. Try selecting more ingredients.")
