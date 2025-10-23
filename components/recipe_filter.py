# components/recipe_filter.py
import pandas as pd
from fuzzywuzzy import fuzz
def filter_recipes(df, selected_ingredients, taste, health_condition):
    """
    Filters the recipes based on:
    - Health condition (optional)
    - Taste preference (optional)
    - Selected ingredients (fuzzy match)
    """
    if df is None or df.empty:
        print("⚠️ Dataset is empty or not loaded.")
        return pd.DataFrame()
    # Handle possible list input for health_condition
    if isinstance(health_condition, list):
        health_condition = health_condition[0] if health_condition else ""
    # Convert to safe lowercase strings
    health_condition = str(health_condition).lower().strip()
    taste = str(taste).lower().strip()
    print(f"🔍 Starting filter: {len(df)} total recipes")
    print(f"Health condition: {health_condition}, Taste: {taste}, Ingredients: {len(selected_ingredients)}")
    # Ensure text columns exist and are lowercase
    df["ingredients"] = df["ingredients"].fillna("").astype(str).str.lower()
    df["taste"] = df["taste"].fillna("").astype(str).str.lower()
    df["health_tags"] = df["health_tags"].fillna("").astype(str).str.lower()
    filtered = df.copy()
    # ✅ 1. Filter by health condition (only if not empty)
    if health_condition and health_condition != "no preference":
        filtered = filtered[filtered["health_tags"].apply(lambda tags: health_condition in tags)]
        print(f"✅ After health condition filter: {len(filtered)} recipes")
    # ✅ 2. Filter by taste (optional)
    if taste and taste != "no preference":
        filtered = filtered[filtered["taste"].str.contains(taste, na=False)]
        print(f"✅ After taste filter: {len(filtered)} recipes")
    # ✅ 3. Fuzzy ingredient matching (relaxed threshold)
    if selected_ingredients:
        selected_ingredients = [i.lower().strip() for i in selected_ingredients]
        def match_score(ingr_str):
            if not ingr_str:
                return 0
            ingr_str = ingr_str.lower()
            matches = sum(fuzz.partial_ratio(i, ingr_str) >= 60 for i in selected_ingredients)
            return matches / len(selected_ingredients)
        filtered["match_score"] = filtered["ingredients"].apply(match_score)
        # ⚠️ Relaxed from 0.2 → 0.05 (so even partial matches show up)
        filtered = filtered[filtered["match_score"] >= 0.05]
        print(f"✅ After ingredient match filter: {len(filtered)} recipes")
    # ✅ If still no matches — return top recipes from dataset instead of blank
    if filtered.empty:
        print("⚠️ No matching recipes found after filtering. Showing sample recipes instead.")
        return df.sample(min(5, len(df)))  # show random 5 recipes as fallback
    # Sort by match score (if available)
    if "match_score" in filtered.columns:
        filtered = filtered.sort_values(by="match_score", ascending=False)
    return filtered
