import streamlit as st

APP_NAME = "HealthRisk AI"
APP_VERSION = "1.0"

PAGE_TITLE = (
    "HealthRisk Lab - Healthcare Financial Intelligence"
)

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

PRIMARY_COLOR = "#1E88E5"

SECONDARY_COLOR = "#43A047"

WARNING_COLOR = "#FB8C00"

DANGER_COLOR = "#E53935"


def configure_page():

    st.set_page_config(
        page_title=PAGE_TITLE,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
        page_icon="🏥"
    )