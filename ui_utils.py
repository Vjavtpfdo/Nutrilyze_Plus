# ui_utils.py
import streamlit as st

def inject_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
          background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836');
          background-size: cover;
          background-position: center;
          background-attachment: fixed;
        }

        .block-container {
          max-width: 980px;
          margin: 1.2rem auto !important;
          background: rgba(255,255,255,0.93);
          border-radius: 14px;
          padding: 2rem 2.2rem;
          box-shadow: 0 10px 30px rgba(0,0,0,0.08);
          backdrop-filter: blur(2px);
        }

        html, body, [class*="css"] {
          color: #000 !important;
          font-family: 'Segoe UI', system-ui, -apple-system, Roboto, Arial, sans-serif;
        }

        .stButton button {
          border-radius: 10px !important;
          padding: .6rem 1rem !important;
          font-weight: 600;
          border: 1px solid #5fbf75 !important;
          background: linear-gradient(180deg, #6ad686, #49b868) !important;
          color: #fff !important;
        }

        .recipe-card {
          background: #fff;
          border: 1px solid #eee;
          border-radius: 12px;
          padding: 1rem;
          margin: 0.5rem 0 1.2rem;
          box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        }

        .recipe-title {
          font-size: 1.3rem;
          font-weight: 700;
          color: #d17b0f !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
