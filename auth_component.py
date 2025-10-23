#auth_component.py
import streamlit as st
import auth_utils  # debugging
from auth_utils import create_user, validate_user, db_info, user_exists


def auth_page():
    st.markdown("## 🔐 User Authentication")
    mode = st.radio("Login / SignUp", ["Login", "SignUp"], horizontal=True)

    with st.form("auth_form", clear_on_submit=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login" if mode == "Login" else "Create Account")

    if submit:
        if mode == "Login":
            if validate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.toast("Login success! Redirecting…", icon="✅")
                st.rerun()
            else:
                st.toast("Invalid credentials.", icon="⚠️")
        else:
            if not username or not password:
                st.toast("Please enter username and password.", icon="⚠️")
            else:
                ok = create_user(username, password)
                if ok:
                    st.toast("Account created. Please login.", icon="✅")
                else:
                    st.toast("Username already exists.", icon="⚠️")

    with st.expander("⚙️ Auth debug (temporary)", expanded=False):
        try:
            path, count = db_info()
            st.caption(f"auth_utils file: {auth_utils.__file__}")
            st.caption(f"DB path: {path}")
            st.caption(f"Users in DB: {count}")
            if username:
                st.caption(f"User exists: {user_exists(username)}")
        except Exception as e:
            st.warning("Debug panel unavailable.")
            st.exception(e)

    if "authenticated" in st.session_state and st.session_state.authenticated:
        st.info(f"Logged in as **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()
