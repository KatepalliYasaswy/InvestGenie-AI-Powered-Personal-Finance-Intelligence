
import streamlit as st
from chatbot.chatbot import get_finance_response


def show_chatbot():

    # ==========================
    # INITIALIZE SESSION STATE
    # ==========================

    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Floating Chat Button */

    .stButton > button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background: linear-gradient(135deg,#ff4b8b,#ff7eb3);
        color: white;
        font-size: 30px;
        border: none;
        z-index: 99999;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }

    /* Chat Window */

    .chat-window {
        position: fixed;
        bottom: 100px;
        right: 20px;
        width: 420px;
        height: 550px;
        background: white;
        border-radius: 20px;
        padding: 15px;
        overflow-y: auto;
        z-index: 9999;
        box-shadow: 0px 5px 30px rgba(0,0,0,0.25);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # FLOATING CHAT BUTTON
    # ==========================

    if st.button("💬", key="floating_chat"):

        st.session_state.chat_open = (
            not st.session_state.chat_open
        )

    # ==========================
    # CHAT WINDOW
    # ==========================

    if st.session_state.chat_open:

        st.markdown(
            '<div class="chat-window">',
            unsafe_allow_html=True
        )

        st.markdown("## 🤖 AI Finance Assistant")

        st.caption(
            "Ask about savings, goals, risk, health score, investments and budgeting."
        )

        # ======================
        # DISPLAY MESSAGES
        # ======================

        for msg in st.session_state.messages:

            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # ======================
        # USER INPUT
        # ======================

        prompt = st.chat_input(
            "Ask me anything about finance..."
        )

        if prompt:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            query = prompt.lower()

            # ======================
            # PERSONALIZED RESPONSES
            # ======================

            if "health score" in query:

                score = st.session_state.get(
                    "health_score",
                    "Not Available"
                )

                response = (
                    f"📊 Your Financial Health Score is: {score}"
                )

            elif "risk" in query:

                risk = st.session_state.get(
                    "risk_score",
                    "Not Available"
                )

                response = (
                    f"⚠️ Your Financial Risk Score is: {risk}"
                )

            elif "behavior" in query:

                behavior = st.session_state.get(
                    "behavior",
                    "Not Available"
                )

                response = (
                    f"🧠 Your spending behavior is classified as: {behavior}"
                )

            elif "goal" in query:

                progress = st.session_state.get(
                    "goal_progress",
                    "Not Available"
                )

                response = (
                    f"🎯 Your goal completion progress is: {progress}%"
                )

            elif "recommendation" in query:

                response = """
✅ Reduce unnecessary spending

✅ Maintain emergency savings

✅ Track monthly expenses

✅ Review financial goals regularly

✅ Diversify investments
"""

            else:

                response = get_finance_response(
                    prompt
                )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )
