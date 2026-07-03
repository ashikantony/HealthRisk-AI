import streamlit as st


def render():

    st.title(
        "Patient Risk Dashboard"
    )

    st.metric(
        "High Risk Patients",
        "2,143",
        "+5%"
    )

    st.metric(
        "Readmission Risk",
        "18%",
        "-2%"
    )