import streamlit as st


def success_alert(message):
    st.success(message)


def warning_alert(message):
    st.warning(message)


def error_alert(message):
    st.error(message)