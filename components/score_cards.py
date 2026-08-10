import streamlit as st


def score_card(title, score, delta):

    st.metric(

        label=title,

        value=score,

        delta=delta

    )


def info_card(title, message):

    st.subheader(title)

    st.info(message)


def success_card(message):

    st.success(message)