import streamlit as st


def display_table(
    dataframe
):

    st.dataframe(
        dataframe,
        use_container_width=True
    )