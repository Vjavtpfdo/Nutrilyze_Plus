# data/load_recipes.py
import pandas as pd

def load_recipes(csv_path="data/recipes2.csv"):
    return pd.read_csv(csv_path)

def filter_recipes(df, health_prefs, taste_prefs, ingredients):
    filtered = df.copy()

    if health_prefs["diet_type"] != "Any":
        filtered = filtered[filtered["diet_type"].str.lower() == health_prefs["diet_type"].lower()]
    
    if health_prefs["allergies"]:
        allergies = [a.strip().lower() for a in health_prefs["allergies"].split(",")]
        filtered = filtered[~filtered["ingredients"].str.lower().str.contains("|".join(allergies))]

    filtered = filtered[filtered["calories"] <= health_prefs["calorie_limit"]]

    if taste_prefs["cuisine"] != "Any":
        filtered = filtered[filtered["cuisine"].str.lower() == taste_prefs["cuisine"].lower()]

    filtered = filtered[filtered["ingredients"].str.lower().str.contains("|".join(i.lower() for i in ingredients))]

    return filtered

'''from pathlib import Path
import pandas as pd

def load_recipes():
    csv_path = Path(__file__).parent / "recipes2.csv"
    return pd.read_csv(csv_path)'''
