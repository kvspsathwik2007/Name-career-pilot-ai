import streamlit as st

from config import client, MODEL


def show_career_coach():

    st.title("🤖 AI Career Coach")

    st.caption(
        "Your personalized AI career strategist"
    )

    st.success(
        "🟢 CAREER COACH ONLINE"
    )

    st.divider()

    # --------------------------------------------------------
    # PROFILE CONTEXT
    # --------------------------------------------------------

    st.subheader("🎯 Career Context")

    col1, col2 = st.columns(2)

    with col1:

        target_role = st.text_input(
            "Target Role",
            placeholder="Example: AI Engineer"
        )

    with col2:

        experience = st.selectbox(
            "Experience Level",
            [
                "Student",
                "Fresher",
                "0-1 Years",
                "1-3 Years",
                "3+ Years"
            ]
        )

    skills = st.text_area(
        "Current Skills",
        placeholder="Python, Java, SQL, Machine Learning..."
    )

    goals = st.text_area(
        "Career Goal",
        placeholder="What do you want to achieve?"
    )

    st.divider()

    # --------------------------------------------------------
    # CHAT
    # --------------------------------------------------------

    st.subheader("💬 Talk to Your Career Coach")

    if "coach_messages" not in st.session_state:

        st.session_state.coach_messages = []

    for message in st.session_state.coach_messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )

    prompt = st.chat_input(
        "Ask your career coach anything..."
    )

    if prompt:

        st.session_state.coach_messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.write(prompt)

        context = f"""
You are CareerPilot AI Career Coach.

Target Role:
{target_role or "Not specified"}

Experience:
{experience}

Current Skills:
{skills or "Not specified"}

Career Goal:
{goals or "Not specified"}

Give practical, personalized career guidance.

User Question:
{prompt}

Rules:
- Be specific.
- Give actionable steps.
- Avoid generic motivational advice.
- If useful, provide a roadmap.
- Keep the response structured.
"""

        try:

            with st.spinner(
                "🧠 Career Coach is thinking..."
            ):

                response = client.chat.completions.create(

                    model=MODEL,

                    messages=[
                        {
                            "role": "system",
                            "content": context
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            answer = (
                response
                .choices[0]
                .message
                .content
            )

        except Exception as error:

            answer = (
                "Unable to contact the AI service.\n\n"
                f"Error: {error}"
            )

        st.session_state.coach_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):

            st.write(answer)

            st.success(
                "Career guidance generated."
            )
            