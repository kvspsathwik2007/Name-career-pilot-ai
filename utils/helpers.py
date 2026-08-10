import streamlit as st


def page_title(title, subtitle=""):

    st.title(title)

    if subtitle:
        st.caption(subtitle)


def section(title):

    st.subheader(title)

    st.divider()