import streamlit as st


def score_ring(
    score,
    label="CAREERPILOT SCORE"
):

    score = int(score or 0)

    score = max(
        0,
        min(100, score)
    )

    angle = score * 3.6

    st.markdown(
        f"""
        <div style="text-align:center">

            <div class="cp-kicker">
                {label}
            </div>

            <div
                class="cp-ring"
                style="
                    --score:{angle}deg;
                    margin-top:14px;
                "
            >

                <div class="cp-ring-inner">

                    <div>

                        <div class="cp-ring-value">
                            {score}
                        </div>

                        <div
                            class="cp-muted"
                            style="font-size:.72rem"
                        >
                            / 100
                        </div>

                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )