import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Set up the Streamlit app
st.set_page_config(page_title="Gowtham's Chatbot", layout="centered")
st.title("🤖 Bhim")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("system", "You are a highly qualified adn experienced ai who can answer to any question with highest accuracy,Your task is to answer all the questions in a understandable way. Your answers plays a major role in somebody life so be conscious and carefull. You are solving the worlds problem.")
    ]

# Chat input (interactive input)
input_txt = st.chat_input("Please enter your query here...")

# Display chat history
for role, msg in st.session_state.chat_history[1:]:  # Skip system prompt
    with st.chat_message(role):
        st.markdown(msg)

# Process input
if input_txt:
    # Add user message to history
    st.session_state.chat_history.append(("user", input_txt))
    with st.chat_message("user"):
        st.markdown(input_txt)

    # Prepare prompt with updated history
    prompt = ChatPromptTemplate.from_messages(st.session_state.chat_history)
    llm = Ollama(model="llama3.2:latest")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # Get response
    response = chain.invoke({"query": input_txt})

    # Add assistant response to history
    st.session_state.chat_history.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)
