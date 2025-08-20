#styles.py
def inject_custom_css():
    import streamlit as st
    st.markdown(
        """
        <style>
        /* App background image */
        .stApp {
          background-image: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836');
          background-size: cover;
          background-position: center;
          background-attachment: fixed;
        }

        /* Center the main container and keep it readable */
        .block-container {
          max-width: 980px;
          margin: 1.2rem auto !important;
          background: rgba(255,255,255,0.93);
          border-radius: 14px;
          padding: 2rem 2.2rem;
          box-shadow: 0 10px 30px rgba(0,0,0,0.08);
          backdrop-filter: blur(2px);
        }

        /* Global text to black */
        html, body, [class*="css"] {
          color: #000 !important;
          font-family: 'Segoe UI', system-ui, -apple-system, Roboto, Arial, sans-serif;
        }
        h1, h2, h3, h4, h5, h6, p, label, span, div, .stMarkdown {
          color: #000 !important;
        }

        /* Inputs/light theme look – prevent dark popovers */
        input, textarea, select {
          background: #fff !important;
          color: #000 !important;
          border: 1px solid #d7d7d7 !important;
          border-radius: 8px !important;
        }
        .stTextInput > div > div input, 
        .stNumberInput input,
        .stDateInput input {
          background: #fff !important;
          color: #000 !important;
          border-radius: 8px !important;
        }
        /* BaseWeb select/multiselect control */
        div[data-baseweb="select"] > div {
          background: #fff !important;
          color: #000 !important;
          border-radius: 10px !important;
          border: 1px solid #d7d7d7 !important;
        }
        /* Dropdown menu panel */
        div[data-baseweb="popover"] {
          background: transparent !important;
        }
        div[data-baseweb="menu"] {
          background: #fff !important;
          color: #000 !important;
          border: 1px solid #e6e6e6 !important;
          box-shadow: 0 10px 20px rgba(0,0,0,0.06) !important;
        }
        /* Selected tags (chips) */
        div[data-baseweb="tag"] {
          background: #f2f8f3 !important;
          color: #0a3816 !important;
          border-radius: 20px !important;
        }

        /* Radio/check labels */
        .stRadio label, .stCheckbox label, .stSelectbox label, .stMultiSelect label {
          color: #000 !important;
          font-weight: 600 !important;
        }

        /* Buttons */
        .stButton button {
          border-radius: 10px !important;
          padding: .6rem 1rem !important;
          font-weight: 600;
          border: 1px solid #5fbf75 !important;
          background: linear-gradient(180deg, #6ad686, #49b868) !important;
          color: #fff !important;
        }
        .stButton button:hover {
          filter: brightness(1.05);
        }

        /* Recipe card */
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
