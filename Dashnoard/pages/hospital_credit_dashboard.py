import streamlit as st


def render():

    st.title(
        "Hospital Credit Dashboard"
    )

    st.metric(
        "Average Credit Score",
        "785"
    )

    st.metric(
        "Default Probability",
        "2.1%"
    )