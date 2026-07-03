import streamlit as st


def render():

    st.title(
        "Healthcare Portfolio Dashboard"
    )

    st.metric(
        "Portfolio Value",
        "$1,245,000"
    )

    st.metric(
        "Monthly Return",
        "7.3%"
    )