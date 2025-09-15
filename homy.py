import streamlit as st
import requests

# --- UI Setup ---
st.set_page_config(page_title="LawGPT", layout="centered")
st.title("📚 LawGPT - Your Legal Assistant")
st.markdown("Ask any legal question related to Indian or global law.")

# --- Input Section ---
question = st.text_area("📝 Enter your legal question here:", height=150)

# --- Helper Function to Format Prompt ---
def format_prompt(question):
    return f"Answer the following legal question based on Indian law:\n{question}"

# --- API Call to NVIDIA NIMs ---
def query_nim(formatted_question):
    url = "https://integrate.api.nvidia.com/v1"  # Replace with actual endpoint
    headers = {
        "Authorization": "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",  # Replace with your actual API key
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": formatted_question,
        "temperature": 0.7,
        "max_tokens": 1024
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("answer", "No answer returned.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# --- Response Section ---
if st.button("🔍 Ask LawGPT"):
    if question.strip():
        with st.spinner("Thinking..."):
            formatted_question = format_prompt(question)
            answer = query_nim(formatted_question)
            st.markdown("### ✅ Answer:")
            st.write(answer)
    else:
        st.warning("Please enter a legal question before submitting.")

# --- Footer ---
st.markdown("---")
st.markdown("Built with ❤️ using NVIDIA NIMs and Streamlit.")
