#components/ingredient_input.py
import streamlit as st

# ----------------- Detailed Ingredients -----------------
INGREDIENTS = {
    "Diabetes": {
    "🍗 Animal Products": [
        "Egg Whites", "Eggs", "Fish", "Salmon" ," Shrimp",
         "Lean Turkey", "Quorn ","Prawns",
        "Seitan (Wheat gluten protein)", "Tempeh", "Tofu", "Turkey", "Turkey Breast"
    ],

    "🥛 Dairy & Alternatives": [
        "Almond Milk", "Butter","Curd", "Ghee","Greek Yogurt", "Kefir", "Kefir Grains",
        "Low-Fat Yogurt", "Milk", "Paneer", "Skimmed Milk", "Yogurt"
    ],

    "🌰 Nuts & Seeds": [
        "Almond Butter", "Almonds", "Cashew", "Chia Seeds", "Chickpeas",
        "Coconut", "Coconut Milk", "Coconut Paste", "Flax Seeds", "Flaxseed Meal",
        "Groundnut", "Makhana ", "Peanuts", "Pistachio",
        "Pumpkin Seeds", "Sesame Seeds", "Sunflower Seeds", "Walnuts"
    ],

    "🫘 Pulses & Legumes": [
        "Black Beans", "Black Gram", "Black Gram Sprouts", "Chana Dal", "Chickpeas",
        "Edamame", "Green Gram", "Horse Gram", "Kidney Beans", "Lentils",
        "Lentil Sprouts", "Masoor Dal", "Moong", "Moong Dal",
        "Rajma Sprouts", "Soybeans", "Soy Chunks", "Sprouted Chickpeas",
        "Sprouted Green Gram", "Sprouted Moong", "Sprouts", "Toor Dal", "Urad Dal"
    ],

    "🌿 Herbs & Leaves": [
        "Basil", "Bay Leaf", "Coriander Leaves", "Curry Leaves", "Drumstick Leaves",
        "Fenugreek Leaves", "Fenugreek Seeds", "Mint Leaves", "Moringa Leaves",
        "Oregano", "Parsley", "Rosemary", "Thyme", "Tulsi Leaves"
    ],

    "🌶️ Spices & Condiments": [
        "Baking Powder", "Baking Soda", "Black Pepper", "Black Salt",
        "Cardamom", "Chaat Masala", "Chili Powder", "Cinnamon", "Cloves",
        "Coriander Powder", "Cumin", "Cumin Powder", "Cumin Seeds",
        "Dry Mango Powder", "Dry Red Chilies", "Garam Masala",
        "Ginger", "Green Chilies", "Lemon", "Mustard Seeds", "Salt",
        "Sambar Powder", "Soy Sauce", "Tamarind", "Tamarind Paste",
        "Turmeric", "Turmeric Powder", "Vanilla", "Vinegar"
    ],

    "🛢️ Oils & Fats": [
        "Coconut Oil", "Groundnut Oil", "Mustard Oil",
        "Olive Oil", "Sesame Oil", "Sunflower Oil"
    ],

    "🥣 Flours & Grains": [
        "Amaranth Flour", "Amaranth Millet", "Amaranth Seeds", "Bajra", "Bajra Flour",
        "Barley", "Barley Flour", "Barnyard Millet", "Besan", "Brown Rice", "Brown Rice Flour",
        "Buckwheat", "Buckwheat Groats", "Buckwheat Flour", "Bulgur", "Dalia",
        "Foxtail Millet", "Foxtail Millet Flour", "Jowar", "Jowar Flour", "Kodo Millet",
        "Little Millet", "Millet", "Millet Flour", "Millet Sprouts", "Oats", "Oats Flour",
        "Pearl Millet", "Pearl Millet Flour", "Quinoa", "Quinoa Flour", "Ragi", "Ragi Flour",
        "Rajgira", "Rajgira Flour", "Rice", "Rice Flour", "Sattu", "Sattu Flour",
        "Semolina", "Wheat", "Wheat Bread", "Wheat Flour", "Whole Wheat Flour", "Wrap Flour"
    ],

    "🌱 Vegetables": [
        "Amaranth Leaves", "Ash Gourd", "Asparagus", "Beetroot", "Bitter Gourd",
        "Bottle Gourd", "Broccoli", "Cabbage", "Capsicum", "Bell Pepper", "Beets",
        "Tomato", "Carrot", "Cauliflower", "Celery", "Colocasia Leaves",
        "Colocasia Stems", "Corn", "Cucumber", "Drumstick", "Drumstick Leaves",
        "Brinjal", "Green Beans", "Green Peas", "Ivy Gourd", "Kale",
        "Lettuce", "Moringa Leaves", "Mushroom", "Okra", "Onion", "Peas",
        "Potato", "Pumpkin", "Radish", "Radish Leaves", "Raw Banana",
        "Ridge Gourd", "Snake Gourd", "Spinach", "Tinda", "Turnip", "Zucchini"
    ],

    "🍎 Fruits & Natural Sweeteners": [
        "Apple", "Avocado", "Banana", "Dates", "Honey", "Jaggery",
        "Lemon", "Mango", "Pineapple", "Strawberries", "Sugar", "Vanilla"
    ],

    "🍯 Others / Extras": [
        "Bread Crumbs", "Coconut", "Coconut Milk", "Coconut Paste",
        "Hummus", "Protein Powder","Tahini"
    ]
},

    "High Cholesterol": {
        "🌿 Herbs & Leaves": [
        "Agathi Keerai","Amaranth Leaves", "Arai Keerai", "Avarakkai", "Basil", "Basil Leaves", "Chakravarthi Keerai",
        "Coriander Leaves", "Curry Leaves", "Dill","Drumstick Leaves","Fenugreek Leaves", "Gongura Leaves",
        "Kaachini Keerai", "Karisalanganni Keerai", "Karuveppilai", "Keezhanelli Keerai",
        "Keerai Leaves", "Mixed Curry Leaves", "Mint Leaves", "Murungai Poo", "Oregano",
        "Oregano Leaves", "Parsley", "Pasalai Keerai", "Peppermint", "Podalangai", "Pulicha Keerai",
        "Rosemary", "Siru Keerai", "Thavasi Keerai", "Thoothuvalai Keerai", "Thuthuvalai Keerai",
        "Thyme", "Vendhaya Keerai"
    ],

    "🍗 Animal Products": [
        "Almond Milk", "Butter", "Buttermilk", "Chicken", "Curd", "Ghee",
        "King Fish", "Mackerel", "Milk", "Paneer", "Sardine", "Seer Fish",
        "Tofu", "Turkey Mince", "White Fish", "Yogurt", "Yogurt Dressing", "Yogurt Starter"
    ],

    "🌶️ Spices & Condiments": [
        "Black Pepper", "Black Pepper Powder", "Black Salt", "Cardamom", "Cardamom Powder",
        "Cloves", "Coriander", "Coriander Powder", "Coriander Seeds", "Cumin", "Cumin Powder",
        "Cumin Seeds", "Curry Masala", "Mustard Powder", "Mustard Seeds", "Red Chili",
        "Red Chili Powder", "Salt", "Tamarind", "Tamarind Paste"
    ],

    "🛢️ Oils & Fats": [
        "Coconut Oil", "Groundnut Oil", "Olive Oil", "Sunflower Oil"
    ],

    "🌰 Nuts & Seeds": [
        "Almonds", "Chia Seeds", "Flax Seeds", "Pumpkin Seeds", "Sesame Seeds", "Sunflower Seeds","Jackfruit Seeds"
    ],

    "🫘 Pulses & Legumes": [
        "Black-Eyed Pea", "Chana Dal", "Chickpea Flour", "Chickpeas",
        "Cowpeas", "Green Gram","Green Moong Dal",
        "Green Gram Sprouts", "Green Moong Sprouts", "Horse Gram ","Sprouted Horse Gram",
        "Lentils","Masoor Dal", "Moong Dal", "Moong Dal Balls", "Moong Sprouts", "Rajma","Kidney Bean",
        "Soy Chunks", "Soybean", "Sprouted Chickpeas", "Sprouted Dal", "Sprouted Lentils",
        "Sprouted Soybeans", "Sprouted Urad Dal", "Sprouted Vegetables",
        "Toor Dal", "Urad Dal", "White Bean"
    ],

    "🥣 Flours & Grains": [
        "Amaranth / Amaranth Flour", "Bajra / Bajra Flour",
        "Barnyard Millet", "Barley", "Brown Rice", "Buckwheat",
        "Bulgur", "Cooked Rice", "Farro", "Foxtail Millet", "Freekeh", "Idli Rice",
        "Jowar","Jowar Flour", "Khorasan Wheat", "Kodo Millet", "Little Millet",
        "Matta Rice", "Millet","Millet Flour"  ,"Sprouted Millet",
        "Navara Red Rice", "Pearl Millet", "Pearl Millet Flour", "Quinoa",
        "Ragi","Ragi Flour", "Red Rice", "Samak Rice",
        "Sorghum", "Spelt", "Teff", "Wheat","Wheat Flour",
        "White Rice", "Whole Wheat Flour",
    ],

    "🌱 Vegetables": [
        "Amla", "Ash Gourd", "Banana Flower", "Banana Stem", "Beans","Green Beans",
        "Beetroot", "Bitter Gourd", "Bottle Gourd", "Brinjal",
        "Broccoli", "Cabbage", "Capsicum","Bell Pepper", "Carrot",
        "Cauliflower", "Chayote", "Corn","Sweet Corn", "Cucumber", "Drumstick","Raw Mango",
        "Gourd", "Horse Gram", "Kale", "Lettuce", "Mushroom", "Okra", "Onion",
        "Plantain", "Potato", "Pumpkin", "Radish", "Raw Banana", "Ridge Gourd",
        "Snake Gourd","Chow-chow","Sponge Gourd","Ivy Gourd","Spinach",
        "Sweet Potato","Yam","Zucchini", "Tomato"
    ],

    "🍎 Fruits": [
        "Apple", "Amla","Banana", "Tender Coconut", "Lemon",
        "Mango", "Orange",
        "Papaya", "Pear", "Pineapple", "Pomegranate"
    ],

    "🍯 Others / Extras": [
        "Bread", "Flatbread", "Coconut Milk","Fermented Millet", "Honey", "Jaggery", "Thinai Sevai", "Tomato Garlic Sauce"
    ]
    },

    "Eye Health": {
    "🌿 Herbs & Leaves": [
        "Curry Leaves", "Coriander Leaves", "Mint Leaves", "Fenugreek Leaves",
        "Drumstick Leaves", "Spinach Leaves", "Cabbage Leaves", "Mustard Leaves",
        "Bathua Leaves", "Amaranth Leaves", "Poi Saag", "Gongura Leaves",
        "Radish Leaves", "Dill Leaves", "Collard Greens", "Bitter Gourd Leaves",
        "Methi Leaves", "Salad Leaves", "Lettuce", "Thyme", "Rosemary"
    ],
    "🍗 Animal Products": [
        "Chicken","Egg","Prawn", "Crab", "Mutton","Mackerel Fish", "Sardine Fish", "Rohu Fish", "Hilsa Fish", "Salmon Fish",
        "Seer Fish", "Pomfret Fish", "Tilapia Fish", "Tuna Fish", "Kingfish","Fish Pieces",
        "Catla Fish",  "Mutton Liver", 
         "Fish Fillet", "Fish Mince", "Fish Balls", "Dry Fish",
        "Dry Anchovy", "Anchovy", "Dry Shrimp", "Turkey"
    ],
    "🛢️ Oils & Fats": [
        "Coconut Oil", "Mustard Oil", "Sunflower Oil", "Ghee", "Groundnut Oil",
        "Olive Oil", "Gingelly Oil", "Almond Oil", "Sesame Oil", "Peanut Oil",
        "Olive coconut oil", "Coconut sesame oil"
    ],
    "🌶️ Spices & Condiments": [
        "Turmeric Powder", "Red Chili Powder", "Coriander Powder", "Cumin Seeds",
        "Cumin Powder", "Black Pepper", "Black Pepper Powder", "Garam Masala",
        "Fenugreek Seeds", "Mustard Seeds", "Cardamom Powder", "Cardamom",
        "Vinegar", "Baking Soda", "Carom Seeds", "Dry Red Chili", "Salt",
        "Sugar", "Jaggery", "Hing", "Chili Powder", "Paprika",
        "Tandoori Masala", "Paprika", "Oregano", "Thyme", "Baking Powder",
        "Spices", "Ginger-Garlic Paste", "Garlic Paste", "Mango Powder",
        "Tamarind", "Tamarind Paste", "Lemon Juice", "Marinade Sauce", "Fish Masala",
        "Turmeric", "Chili",  "Mustard greens",  "Leaf"
    ],
    "🌰 Nuts & Seeds": [
        "Cashew Nuts", "Almonds", "Walnut", "Flaxseeds", "Sesame Seeds",
        "Chia Seeds"
    ],
    "🫘 Pulses & Legumes": [
        "Toor Dal", "Moong Dal", "Chana Dal", "Masoor Dal", "Urad Dal",
        "Chickpeas", "Green Gram", "Horse Gram", "Soya Bean", "Soya Granules","Panchmel dal",
        "Soya Protein", "Lentils", "Rajma", "Dal", "Chickpea Flour", "Besan", "Gram Flour", "Lentil"
    ],
    "🥛 Dairy & Alternatives": [
        "Curd", "Yogurt", "Paneer", "Milk", "Cream", "Buttermilk",
        "Almond Milk", "Ricotta Cheese", "Cheese", "Condensed Milk",
        "Sweetener", "Vanilla", "Ice Cream", "Butter"
    ],
    "🥣 Flours & Grains": [
        "Wheat Flour", "Rice Flour", "Ragi Flour", "Bajra", "Jowar Flour",
        "Semolina", "Quinoa", "Brown Rice", "Red Rice", "Basmati Rice", "Rice",
        "Maize Flour", "Gram Flour", "Besan", "Oats","Oats Flour",
        "Bread","Wheat Bread", "Rice Paper", "Rice Batter", "Fermented Batter"
    ],
    "🌱 Vegetables": [
        "Onion", "Tomato", "Potato","Carrot", "Beans", "Capsicum" , 
        "Brinjal","Bell Pepper","Garlic", "Ginger", "Green Chili", 
        "Pumpkin", "Bottle Gourd", "Bitter Gourd", "Ridge Gourd",
        "Green Beans",  "Cucumber",
        "Snake Gourd", "Lotus Stem", "Okra", "Broccoli", "Cauliflower",
        "Turnip", "Mushroom", "Sweet Corn", "Papaya", "Banana Flower",
        "Banana Stem", "Jackfruit Seeds", "Zucchini", "Yam", "Drumstick"
    ],
    "🍎 Fruits": [
        "Lemon", "Orange", "Honey Orange", 
        "Guava", "Honey Guava", "Raw Mango", "Honey Raw Mango", "Pineapple",
        "Apple", "Mango", "Pomegranate", "Watermelon", "Musk Melon",
        "Custard Apple", "Banana", "Dates", "Strawberry", "Amla", "Berries",
        "Raw Banana", "Jackfruit"
    ],
    "🍯 Others / Extras": [
        "Tamarind", "Tamarind Pulp", "Tamarind Paste", "Coconut", "Coconut Milk",
        "Grated Coconut", "Bread Crumbs", "Cooked Rice", "Rice Batter",
        "Uttapam Batter", "Dosa Batter", "Honey", "Soy Sauce", "Broth",
        "Mayonnaise", "Skewers", "Cornstarch"
    ]
},

    "Hypothyroid": {
    "🌿 Herbs & Leaves": [
        "Coriander Leaves", "Curry Leaves", "Methi", "Mint",
        "Parsley", "Tulsi", "Agathi Green", "Agathi Greens Leave",
        "Amaranth", "Amaranth Leave", "Arai Green", "Betel Leave",
        "Drumstick Leave", "Dwarf Copperleaf Green", "False Daisy Green",
        "Indian Nettle Green", "Manathakkali Green", "Moringa Leave",
        "Mudakathan Green", "Mustard Green", "Murungai Green",
        "Palak", "Ponnanganni Green", "Solanum Trilobatum",
        "Spinach", "Small Green", "Taro Leave", "Vallarai Green",
        "Vallarai Leave"
    ],

    "🍗 Animal Products & Seafood": [
        "Beef", "Chicken", "Chicken Breast", "Egg", "Eggs", "Mutton",
        "Paneer", "Turkey", "Anchovy Fish", "Cod", "Fish", "Fish Roe",
        "Mackerel Fish", "Oyster", "Pearl Spot Fish", "Pomfret",
        "Salmon", "Sardine Fish", "Seaweed", "Seer Fish", "Shrimp", "Tuna"
    ],

    "🌾 Flours & Grains": [
        "Brown Rice", "Foxtail Millet", "Kodo Millet", "Little Millet",
        "Millet", "Navara Rice", "Oat", "Pearl Millet", "Quinoa",
        "Ragi", "Rava", "Rice", "Rice Flour", "Semolina",
        "String Hopper", "White Rice", "Gram Flour"
    ],

    "🫘 Pulses & Legumes": [
        "Bengal Gram", "Black Gram", "Black-Eyed Pea", "Broad Bean",
        "Chickpea", "Cowpea", "Dried Pea", "Gram", "Horse Gram",
        "Lentil", "Masoor Dal", "Moong Dal", "Pigeon Pea",
        "Red Gram", "Roasted Gram", "Toor Dal", "Urad Dal"
    ],

    "🥛 Dairy & Alternatives": [
        "Buttermilk", "Curd", "Milk", "Yogurt", "Ghee"
    ],

    "🌰 Nuts & Seeds": [
        "Brazil Nut", "Cashew", "Coconut", "Flax Seed",
        "Groundnut", "Jackfruit Seed", "Pumpkin Seed",
        "Sesame Seeds", "Nuts"
    ],

    "🍅 Vegetables & Greens": [
        "Ash Gourd", "Bamboo Shoot", "Beetroot", "Bell Pepper",
        "Bitter Gourd", "Bottle Gourd", "Bottle Gourd Leave",
        "Carrot", "Chayote", "Colocasia", "Cucumber", "Drumstick",
        "Drumstick Seed", "Eggplant", "Ivy Gourd", "Lady Finger",
        "Malabar Spinach", "Mushroom", "Okra", "Pointed Gourd",
        "Potato", "Pumpkin", "Pumpkin Leave", "Radish", "Red Pumpkin",
        "Ridge Gourd", "Snake Gourd", "Tindora", "Tomato", "Yam"
    ],

    "🍎 Fruits & Natural Sweeteners": [
        "Avocado", "Berrie", "Guava", "Honey", "Jaggery",
        "Raisin"
    ],

    "🌶️ Spices & Condiments": [
        "Asafoetida", "Black Pepper", "Cardamom", "Chili",
        "Chili Powder", "Clove", "Coriander Powder", "Cumin",
        "Cumin Seeds", "Fennel Seeds", "Fenugreek Seeds",
        "Garam Masala", "Garlic", "Ginger", "Ginger Garlic Paste",
        "Iodized Salt", "Lemon", "Mustard Seeds", "Pepper",
        "Salt", "Sambar Powder", "Saffron", "Tamarind",
        "Turmeric", "Turmeric Powder", "Parsley"
    ],

    "🛢️ Oils & Fats": [
        "Coconut Oil", "Ghee", "Groundnut Oil", "Refined Oil",
        "Sesame Oil", "Sunflower Oil"
    ],

    "🍯 Others": [
        "Coconut Milk", "Water", "Sugar"
    ]
}

}

# ----------------- UI Function -----------------
def get_selected_ingredients(condition: str | None) -> list:
    """Display ingredient selection based on the chosen health condition."""

    # --- Normalize key ---
    key_map = {
        "Hypothyroid": "Hypothyroidism",  # map to INGREDIENTS key if needed
        "Hypothyroidism": "Hypothyroid",  # if condition comes from DATA_MAP
    }

    normalized_condition = key_map.get(condition, condition)

    st.subheader(f"🛒 Select Ingredients for {normalized_condition if normalized_condition else 'your condition'}")

    if not normalized_condition or normalized_condition not in INGREDIENTS:
        st.warning("⚠️ Please select a valid health condition to view ingredients.")
        return []

    selected_ingredients = {}
    for category, items in INGREDIENTS[normalized_condition].items():
        selected = st.multiselect(
            f"{category}",
            items,
            default=items[:1],
            key=f"{normalized_condition}_{category}_{hash(category)}"
        )
        if selected:
            selected_ingredients[category] = selected

    final_list = list(dict.fromkeys(
        [item for sublist in selected_ingredients.values() for item in sublist] + ["Salt"]
    ))

    st.success(f"✅ {len(final_list)} ingredients selected.")
    return final_list
