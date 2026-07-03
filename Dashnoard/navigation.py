import streamlit as st


class DashboardNavigation:

    PAGES = [
        "Home",
        "Patient Risk",
        "Insurance",
        "Hospital Credit",
        "Pharmaceutical",
        "ESG Analytics",
        "Portfolio",
        "Simulation",
        "Explainability",
        "Monitoring"
    ]

    @staticmethod
    def menu():

        return st.sidebar.radio(
            "Navigation",
            DashboardNavigation.PAGES
        )