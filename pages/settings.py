import streamlit as st


def show_settings():

    st.title("⚙ Settings")

    st.write("Theme")

    st.selectbox(

        "Theme",

        [
            "Dark",
            "Light"
        ]

    )

    st.write("Version 1.0")