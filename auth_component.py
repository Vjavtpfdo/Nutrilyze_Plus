#auth_component.py
import streamlit as st
from auth_utils import create_user, validate_user

def auth_page():
    st.markdown("## 🔐 User Authentication")
    mode = st.radio("Login / SignUp", ["Login", "SignUp"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    if mode == "Login":
        if col1.button("Login"):
            if validate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success("Login success! Redirecting…")
                st.rerun()
            else:
                st.error("Invalid credentials.")
    else:
        if col1.button("Create Account"):
            if not username or not password:
                st.warning("Please enter username and password.")
            else:
                ok = create_user(username, password)
                if ok:
                    st.success("Account created. Please login.")
                else:
                    st.error("Username already exists.")

    if "authenticated" in st.session_state and st.session_state.authenticated:
        st.info(f"Logged in as **{st.session_state.username}**")
        if col2.button("Logout"):
            st.session_state.clear()
            st.rerun()
