import streamlit as st


def telemetry_card(
    icon,
    label,
    score,
    status=""
):
    score = int(score or 0)

    display_score = score if score > 0 else "—"

    status_text = (
        status
        if status
        else (
            "Awaiting analysis"
            if score == 0
            else "Telemetry synchronized"
        )
    )

    st.markdown(
        f"""
        <div class="cp-card">

            <div class="cp-kicker">
                {icon} {label.upper()}
            </div>

            <div
                style="
                    font:700 2rem 'Space Grotesk';
                    margin-top:8px;
                "
            >
                {display_score}

                <span
                    class="cp-muted"
                    style="font-size:.8rem"
                >
                    / 100
                </span>
            </div>

            <div
                style="
                    height:5px;
                    background:rgba(148,163,184,.12);
                    border-radius:99px;
                    margin-top:12px;
                    overflow:hidden;
                "
            >

                <div
                    style="
                        width:{score}%;
                        height:100%;
                        border-radius:99px;
                        background:
                            linear-gradient(
                                90deg,
                                #8b5cf6,
                                #06b6d4
                            );
                        box-shadow:
                            0 0 12px
                            rgba(6,182,212,.35);
                    "
                ></div>

            </div>

            <div
                class="cp-muted"
                style="margin-top:8px"
            >
                {status_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )