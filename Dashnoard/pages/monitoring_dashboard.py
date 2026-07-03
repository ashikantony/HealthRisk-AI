import streamlit as st


def render():

    st.title(
        "Real-Time Monitoring"
    )

    st.metric(
        "API Status",
        "Online"
    )

    st.metric(
        "Model Latency",
        "38 ms"
    )