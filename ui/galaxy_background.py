import streamlit as st


def render_galaxy_background():

    st.markdown(
        """
        <div
            style="
                position:fixed;
                inset:0;
                pointer-events:none;
                z-index:0;

                background:

                    radial-gradient(
                        circle at 20% 30%,
                        rgba(139,92,246,.08),
                        transparent 22%
                    ),

                    radial-gradient(
                        circle at 80% 60%,
                        rgba(6,182,212,.07),
                        transparent 24%
                    );
            "
        ></div>
        """,
        unsafe_allow_html=True,
    )