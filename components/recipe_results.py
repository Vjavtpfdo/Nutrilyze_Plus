#components/recipe_results.py
import streamlit as st
import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/recipes2.csv")

def _load_df():
    if not CSV_PATH.exists():
        st.error(f"Recipe dataset not found at `{CSV_PATH}`.")
        return pd.DataFrame()
    df = pd.read_csv(CSV_PATH)
    # normalize lowercase for ingredients
    df["ingredients_list"] = df["ingredients"].str.lower().str.split(",")
    # normalize health tags
    df["health_list"] = df["health_tags"].str.split(",").apply(lambda xs: [x.strip() for x in xs])
    return df

def show_matched_recipes(health_condition, taste_preference, selected_ingredients):
    df = _load_df()
    if df.empty:
        return

    sel = [x.strip().lower() for x in selected_ingredients]
    # Filter by health condition (if not 'None')
    if health_condition != "None":
        df = df[df["health_list"].apply(lambda tags: health_condition in tags)]

    # Filter by taste (if not 'No Preference')
    if taste_preference != "No Preference":
        df = df[df["taste"].str.contains(taste_preference.split()[0], case=False)]

    # 75% ingredient match
    def pct_match(row):
        ing = set([x.strip() for x in row["ingredients_list"] if x.strip()])
        match = ing.intersection(set(sel))
        return (len(match) / max(len(ing), 1)) >= 0.75

    df = df[df.apply(pct_match, axis=1)]

    if df.empty:
        st.warning("❌ No matching recipes found. Try adjusting taste/health or add more ingredients.")
        return

    st.subheader("🍽 Recommended Recipes for You:")
    for _, r in df.iterrows():
        col1, col2 = st.columns([1, 2])
        with col1:
            # Placeholder image by first word fallback
            st.image(f"https://source.unsplash.com/400x250/?healthy,{r['name'].split()[0]}",
                     use_container_width=True)
        with col2:
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='recipe-title'>🍽 {r['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"🔥 **Calories:** {int(r['calories'])} kcal")
            st.markdown(f"😋 **Taste:** {r['taste']}")
            st.markdown(f"🩺 **Health Tags:** {r['health_tags']}")
            st.markdown(f"🧂 **Ingredients:** {r['ingredients']}")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")
