import streamlit as st


def render_sidebar():

    st.sidebar.image(
        "dashboard/assets/logo.png",
        width=120
    )

    st.sidebar.title(
        "HealthRisk AI"
    )

    st.sidebar.markdown(
        "---"
    )