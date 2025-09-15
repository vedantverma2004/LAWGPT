import streamlit as st
import requests
 
# 🔐 Embedded NVIDIA API Key (replace with your actual key)
NVIDIA_API_KEY = "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"
# Streamlit UI
st.set_page_config(page_title="LawGPT - Legal Q&A", layout="centered")
st.title("🧠 LawGPT - Legal Question Answering")
st.markdown("Ask law-based questions and get intelligent answers powered by NVIDIA's LLM.")
 
# Input field for the legal question
question = st.text_area("📜 Enter your legal question")
 
# Submit button
if st.button("Ask"):
    if not question.strip():
        st.warning("⚠️ Please enter a legal question before submitting.")
    else:
        payload = {
            "model": "nvidia/llama3-chatqa-1.5-70b",
            "messages": [{"role": "user", "content": question}]
        }
        headers = {
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Content-Type": "application/json"
        }
 
        with st.spinner("🔍 Getting answer from NVIDIA LLM..."):
            try:
                response = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                answer = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                st.success("✅ Response:")
                st.write(answer)
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error communicating with NVIDIA API: {str(e)}")
 
