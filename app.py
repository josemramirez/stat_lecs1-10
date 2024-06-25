import streamlit as st
from openai import OpenAI
import time

# Create client
client = OpenAI(api_key='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')

st.title(':Thermodynamics-Software: Lectures 1-10')

# Initialize chat history (using session_state)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.container():
        st.markdown(f"**{message['role']}:** {message['content']}")

# Input text box
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message immediately
    with st.container():
        st.markdown(f"**You:** {user_input}")

    # Create thread and message 
    thread = client.beta.threads.create()
    thread_message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id='asst_u8xyGCwd7SQfH12N4IDY2VvO'  # Replace with your assistant ID
    )
    
    # Wait for the run to complete
    with st.spinner("Thinking..."):
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(0.5)

    # Retrieve and display the response
    messages = client.beta.threads.messages.list(thread_id=thread.id).data
    latest_message = messages[0]
    response_text = latest_message.content[0].text.value

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    # Clear the input text box after sending
    user_input = ""

    # Display assistant message immediately
    with st.container():
        st.markdown(f"**Assistant:** {response_text}")
