import pandas as pd

def load_recipes():
    df = pd.read_csv("data/recipes2.csv")  # Make sure path is correct
    recipes = []

    for _, row in df.iterrows():
        recipe = {
            "name": row["name"],
            "ingredients": [i.strip().lower() for i in row["ingredients"].split(",")],
            "calories": row["calories"],
            "protein": row["protein"],
            "fat": row["fat"],
            "carbohydrates": row["carbohydrates"],
            "taste": row["taste"],
            "health_tags": [h.strip() for h in str(row["health_tags"]).split(",")]
        }
        recipes.append(recipe)

    return recipes
