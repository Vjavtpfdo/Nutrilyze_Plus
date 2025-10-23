# components/health_form.py
import streamlit as st

def get_user_health_inputs():
    st.markdown("<h2 style='text-align: center;'>💊 Select Your Health Condition</h2>", unsafe_allow_html=True)

    conditions = {
        "Diabetes": "🚫 Low sugar, focus on balanced meals",
        "High Cholesterol": "❤️ Heart healthy & low-fat options",
        "Eye Health": "👀 Rich in Vitamin A & antioxidants",
        "Hypothyroidism": "🌀 Balanced iodine & metabolism-friendly foods",
    }

    # initialize
    if "health_condition" not in st.session_state:
        st.session_state.health_condition = None

    cols = st.columns(2)
    for i, (cond, desc) in enumerate(conditions.items()):
        with cols[i % 2]:
            # show as big button
            if st.button(cond, key=f"cond_{cond}", use_container_width=True):
                st.session_state.health_condition = cond
            st.markdown(
                f"<div style='background:#f9f9f9; border-radius:12px; padding:10px; text-align:center; font-size:14px;margin-top:6px'>{desc}</div>",
                unsafe_allow_html=True
            )

    if st.session_state.get("health_condition"):
        st.success(f"✅ Selected: {st.session_state.health_condition}")

    return st.session_state.get("health_condition")
