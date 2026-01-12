
import streamlit as st
from dialogue_manager.dialogue_handler import handle_user_message


def chatbot_ui():
    st.markdown("<h2>💬 BankBot AI Chat</h2>", unsafe_allow_html=True)

    # -------------------------------
    # SAFETY: session defaults
    # -------------------------------
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.warning("🔐 Please login to use the chatbot.")
        return

    # -------------------------------
    # Chat history state
    # -------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "bot", "content": "👋 Hi! Ask me anything about banking."}
        ]

    # -------------------------------
    # Display messages
    # -------------------------------
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"🧑‍💻 **You:** {msg['content']}")
        else:
            st.markdown(f"🤖 **Bot:** {msg['content']}")

    st.markdown("---")

    # -------------------------------
    # Input area
    # -------------------------------
    user_input = st.text_input(
        "Type your question",
        key="chat_input"
    )

    send = st.button("Send 🚀")

    # -------------------------------
    # Message handling
    # -------------------------------
    if send and user_input.strip():
        # Add user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Generate bot reply safely
        try:
            reply = handle_user_message(user_input)
        except Exception as e:
            reply = "⚠️ Sorry, something went wrong."

        # Add bot reply
        st.session_state.messages.append(
            {"role": "bot", "content": reply}
        )

        # Clear input safely
        st.session_state.chat_input = ""

        st.rerun()
