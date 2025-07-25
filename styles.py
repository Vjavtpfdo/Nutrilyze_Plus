def inject_custom_css():
    import streamlit as st
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #fdfaf6;
        }

        .stApp {
            background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836');
            background-size: cover;
            background-position: top;
            background-attachment: fixed;
        }

        .block-container {
            background-color: rgba(255,255,255,0.92);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        }

        .recipe-card {
            background-color: #ffffff;
            border: 1px solid #eee;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }

        .recipe-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #d17b0f;
        }

        </style>
    """, unsafe_allow_html=True)
