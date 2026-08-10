import streamlit as st


def primary_button(text):

    return st.button(

        text,

        use_container_width=True

    )


def secondary_button(text):

    return st.button(

        text

    )