import streamlit as st

from generating_syllabus import generate_syllabus
from teaching_agent import teaching_agent


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Tutor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Your AI Instructor")


# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "syllabus_generated" not in st.session_state:
    st.session_state.syllabus_generated = False


# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Generate Syllabus", "AI Instructor"]
)


# =========================================================
# PAGE 1 : GENERATE SYLLABUS
# =========================================================

if page == "Generate Syllabus":

    st.header("Generate Learning Syllabus")

    topic = st.text_input(
        "Enter topic you want to learn"
    )

    if st.button("Generate Syllabus"):

        if topic.strip() == "":
            st.warning("Please enter a topic")
        else:

            with st.spinner("Generating syllabus..."):

                task = f"Teach the topic: {topic}"

                syllabus = generate_syllabus(topic, task)

                teaching_agent.seed_agent(syllabus, topic)

                st.session_state.syllabus_generated = True
                st.session_state.syllabus = syllabus

            st.success("Syllabus generated successfully!")

    if "syllabus" in st.session_state:

        st.subheader("Generated Syllabus")

        st.text_area(
            "",
            value=st.session_state.syllabus,
            height=400
        )


# =========================================================
# PAGE 2 : AI INSTRUCTOR CHAT
# =========================================================

elif page == "AI Instructor":

    st.header("Ask Questions to AI Instructor")

    if not st.session_state.syllabus_generated:
        st.warning("Please generate syllabus first.")
    else:

        # DISPLAY CHAT HISTORY
        for chat in st.session_state.chat_history:

            with st.chat_message("user"):
                st.markdown(chat["user"])

            with st.chat_message("assistant"):
                st.markdown(chat["bot"])

        # USER INPUT
        user_question = st.chat_input(
            "Ask your question"
        )

        if user_question:

            # SHOW USER MESSAGE
            with st.chat_message("user"):
                st.markdown(user_question)

            # SEND TO AGENT
            teaching_agent.human_step(user_question)

            # GET BOT RESPONSE
            with st.chat_message("assistant"):

                message_placeholder = st.empty()

                bot_response = teaching_agent.instructor_step()

                full_response = ""

                for char in bot_response:

                    full_response += char

                    

                    message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

            # SAVE CHAT
            st.session_state.chat_history.append(
                {
                    "user": user_question,
                    "bot": full_response
                }
            )

        # CLEAR CHAT BUTTON
        if st.button("Clear Chat"):

            st.session_state.chat_history = []

            st.rerun()