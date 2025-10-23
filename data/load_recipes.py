# data/load_recipes.py
import pandas as pd
from pathlib import Path
from typing import List

# ----------------- Paths for each health condition -----------------
DATA_DIR = Path("data")
DATA_MAP = {
    "diabetes": "diabetes_recipes.csv",
    "high cholesterol": "cholesterol_recipes.csv",
    "eye health": "eyehealth_recipes1.csv",
    "hypothyroidism": "hypothyroidism_recipes.csv",
}

# ----------------- Loader & Cleaner (Robust Version) -----------------
def load_recipes(condition: str) -> pd.DataFrame:
    """
    Load and clean recipe dataset for a given health condition.
    Args:
        condition (str): Health condition (e.g., "eye health").
    Returns:
        pd.DataFrame: Cleaned recipe DataFrame
    """
    condition_key = condition.strip().lower()
    expected_filename = DATA_MAP.get(condition_key)

    if not expected_filename:
        print(f"⚠️ No mapping for condition '{condition_key}'")
        return pd.DataFrame()

    # Check data folder
    if not DATA_DIR.exists():
        print(f"❌ Data folder not found: {DATA_DIR.resolve()}")
        return pd.DataFrame()

    # Try to find the file (case-insensitive and partial match)
    matched_files = [
        f for f in DATA_DIR.iterdir()
        if f.is_file() and expected_filename.lower().replace("_","") in f.name.lower().replace("_","")
    ]

    if not matched_files:
        print(f"⚠️ No dataset found for '{condition}'. Expected: '{expected_filename}' in {DATA_DIR}/")
        print("📂 Available files:", [f.name for f in DATA_DIR.iterdir()])
        return pd.DataFrame()

    path = matched_files[0]

    # Read CSV with fallback encoding
    try:
        df = pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="latin1")

    print(f"✅ Loaded '{condition}' dataset successfully! Rows: {len(df)} | Columns: {list(df.columns)}")
    # ----------------- Standardize column names -----------------
    rename_map = {
        "Food Name": "name",
        "food_name": "name",
        "Ingredients": "ingredients",
        "ingredients": "ingredients",
        "Prep Time": "prep_time",
        "prep_time": "prep_time",
        "Calories": "calories",
        "calories": "calories",
        "Protein_g": "protein_g",
        "Protein (g)": "protein_g",
        "protein": "protein_g",
        "Fat": "fat_g",
        "fat": "fat_g",
        "Carbohydrates_g": "carbs_g",
        "Carbohydrates (g)": "carbs_g",
        "taste": "taste",
        "Taste": "taste",
        "Instruction": "instructions",
        "Instructions": "instructions",
        "Description": "description",
        "No_serving": "serves",
        "Serves": "serves",
        "Health Tags": "health_tags",
        "health_tags": "health_tags",
    }
    df = df.rename(columns=rename_map)

    # ----------------- Ensure required columns exist -----------------
    essential_cols = [
        "name", "ingredients", "taste", "instructions",
        "description", "health_tags", "calories",
        "protein_g", "fat_g", "carbs_g", "serves"
    ]
    for c in essential_cols:
        if c not in df.columns:
            df[c] = ""

    # ----------------- Fill and clean text columns -----------------
    text_cols = ["ingredients", "taste", "instructions", "description", "health_tags"]
    for col in text_cols:
        df[col] = df[col].fillna("").astype(str)

    # ----------------- Preprocess list columns -----------------
    def to_list(x):
        if isinstance(x, str):
            return [i.strip() for i in x.lower().split(",") if i.strip()]
        return []

    df["ingredients_list"] = df["ingredients"].apply(to_list)
    df["health_list"] = df["health_tags"].apply(to_list)

    # ----------------- ✅ IMPROVED NUMERIC CLEANING -----------------
    for col in ["calories", "protein_g", "fat_g", "carbs_g"]:
        if col in df.columns:
            # remove text units like 'kcal', 'g', etc., then extract numeric part
            df[col] = (
                df[col]
                .astype(str)
                .str.extract(r"(\d+\.?\d*)")[0]   # only numbers
                .astype(float)
            )

    # ----------------- Add placeholder for match_score -----------------
    df["match_score"] = 0.0

    # Final check
    print(f"🧾 Cleaned '{condition}' dataset: {len(df)} rows, {len(df.columns)} columns")
    return df

# ----------------- Debug Mode Run -----------------
if __name__ == "__main__":
    print(f"\n📂 Checking data folder: {DATA_DIR.resolve()}")
    if DATA_DIR.exists():
        print("✅ Files found:", [f.name for f in DATA_DIR.iterdir()])
    else:
        print("❌ Data folder does not exist!")

    for test_cond in DATA_MAP.keys():
        print(f"\n🔍 Testing load for: {test_cond}")
        df = load_recipes(test_cond)
        if df.empty:
            print(f"❌ Failed to load {test_cond}")
        else:
            print(f"✅ Success: {df.shape} | Sample columns: {list(df.columns)[:6]}")
