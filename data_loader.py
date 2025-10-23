# data_loader.py
import pandas as pd
import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    # collapse multiple spaces and trim
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def estimate_calories(ingredients) -> str:
    """
    Very simple estimator for demo purposes.
    Counts number of distinct ingredients and multiplies by a base value.
    Return string to show when dataset doesn't contain calories.
    """
    try:
        if not ingredients or str(ingredients).strip() == "":
            return "Not Available"
        ing_list = [x.strip() for x in str(ingredients).split(",") if x.strip()]
        est = 50 * max(1, len(set(ing_list)))
        return str(est)
    except Exception:
        return "Not Available"
    