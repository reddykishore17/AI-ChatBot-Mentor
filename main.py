import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# PAGE CONFIG — Added ICON
st.set_page_config(
    page_title="AI Mentor Assistant",
    page_icon="🤖",
    layout="centered")

MODULES = [
    "Python",
    "SQL",
    "Power BI",
    "Exploratory Data Analysis (EDA)",
    "Machine Learning (ML)",
    "Deep Learning (DL)",
    "Generative AI (Gen AI)",
    "Agentic AI",]

def get_prompt(module_name):
    return ChatPromptTemplate.from_messages([
        (
            "system",
            f"""
You are an expert AI Mentor specializing ONLY in the topic: {module_name}.

Strict rules:
1. You must answer only questions related to {module_name}.
2. If the question is unrelated, reply EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."
3. Keep responses clear, precise, and helpful.
4. No extra information outside the topic.
"""
        ),
        ("human", "{question}")
    ])

# ---------------- SESSION STATES ---------------- #
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False

if "first_message_sent" not in st.session_state:
    st.session_state.first_message_sent = False


# ---------------- MODULE SELECTION ---------------- #
if st.session_state.selected_module is None:

    st.title("Hi, Welcome to AI Chatbot Mentor🧑‍🏫")
    st.subheader("Your dedicated AI-powered learning assistant.")

    selected = st.selectbox("🔍Please choose a module below to begin your mentoring session", MODULES)

    if st.button("▶️ Start Mentoring"):
        st.session_state.selected_module = selected
        st.rerun()

# ---------------- CHAT SCREEN ---------------- #
else:
    module = st.session_state.selected_module

    st.title(f"{module} ChatBot Mentor 🤖")
    st.write(f"Welcome to your **{module} Learning Mentor**. Ask anything related to this topic.")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0)

    prompt = get_prompt(module)

    # Display chat history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    # ---------------- CHAT INPUT (DISABLED AFTER END) ---------------- #
    if not st.session_state.conversation_ended:
        user_input = st.chat_input("💬 Ask your question here...")
    else:
        user_input = None
        st.info("🔒 The conversation has ended. You may download the discussion below.")

    # ---------------- HANDLE USER MESSAGE ---------------- #
    if user_input:
        st.session_state.first_message_sent = True   # Enable End Conversation button

        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        response = llm.invoke(prompt.format_messages(question=user_input))
        ai_reply = response.content

        st.session_state.chat_history.append(("assistant", ai_reply))
        with st.chat_message("assistant"):
            st.markdown(ai_reply)

    # ---------------- END CONVERSATION BUTTON ---------------- #
    if st.session_state.first_message_sent and not st.session_state.conversation_ended:
        if st.button("🔚 End Conversation"):
            st.session_state.conversation_ended = True
            st.rerun()

    # ---------------- DOWNLOAD BUTTON (ONLY AFTER END) ---------------- #
    if st.session_state.conversation_ended and st.session_state.chat_history:
        chat_text = ""
        for role, msg in st.session_state.chat_history:
            label = "User" if role == "user" else "AI Mentor"
            chat_text += f"{label}: {msg}\n\n"

        st.download_button(
            label="📩 Download Conversation",
            data=chat_text,
            file_name=f"{module}_AI_Mentor_Chat.txt",
            mime="text/plain")

    # ---------------- RESET SESSION ---------------- #
    if st.button("🔄 Change Module / Restart"):
        st.session_state.selected_module = None
        st.session_state.chat_history = []
        st.session_state.conversation_ended = False
        st.session_state.first_message_sent = False
        st.rerun()
