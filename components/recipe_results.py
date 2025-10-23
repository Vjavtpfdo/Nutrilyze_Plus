# components/recipe_results.py
import streamlit as st
from data.load_recipes import load_recipes
from components.recipe_filter import filter_recipes
def show_matched_recipes(health_condition, taste_preference, selected_ingredients):
    df = load_recipes(health_condition)
    if df.empty:
        st.error(f"No dataset found for {health_condition}. Please upload recipes into the data/ folder.")
        return
    filtered = filter_recipes(df, health_condition, taste_preference, selected_ingredients)
    if filtered.empty:
        st.warning("❌ No matching recipes found. Try fewer/other ingredients or 'No Preference' for taste.")
        return
    st.subheader("🍽 Recommended Recipes for You:")
    for _, r in filtered.iterrows():
        col1, col2 = st.columns([1, 2])
        with col1:
            name_terms = "+".join(str(r.get("name", "healthy food")).split())
            st.image(f"https://source.unsplash.com/400x250/?healthy,{name_terms}", use_container_width=True)
        with col2:
            st.markdown(f"### 🍽 {r.get('name','Unnamed')}")
            st.markdown(f"**Description:** {r.get('description','-')}")
            st.markdown(f"**Prep Time:** {r.get('prep_time','-')} | **Serves:** {r.get('serves','-')}")
            st.markdown(f"**Calories:** {r.get('calories','-')} | **Protein:** {r.get('protein_g','-')} g")
            st.markdown(f"**Fat:** {r.get('fat_g','-')} g | **Carbs:** {r.get('carbs_g','-')} g")
            st.markdown(f"**Taste:** {r.get('taste','-')}")
            st.markdown(f"**Ingredients:** {r.get('ingredients','-')}")
        instr = r.get("instructions", "-")
        if instr and isinstance(instr, str):
            steps = [s.strip() for s in instr.split(".") if s.strip()]
            st.markdown("**Instructions:**")
            for i, step in enumerate(steps, 1):
                st.markdown(f"{i}. {step}")
        st.markdown("---")
