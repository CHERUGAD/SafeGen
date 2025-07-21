import streamlit as st
import requests

st.set_page_config(page_title="SafeGen", page_icon="🔐")

st.title("🔐 SafeGen: Prompt Safety Checker")
st.markdown("Check if your prompt is safe to generate using AI.")

# Input prompt
prompt = st.text_area("Enter a prompt to check:", height=150)

# Submit button
if st.button("Check Safety"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        try:
            # Call the FastAPI endpoint
            response = requests.post(
                "http://localhost:8000/check_prompt",
                json={"prompt": prompt}
            )
            response.raise_for_status()  # Raise error if status code is not 200
            data = response.json()

            if data.get("is_safe", False):
                st.success("✅ This prompt is safe.")
            else:
                st.error("🚫 Unsafe prompt detected! Access denied.")
        except Exception as e:
            st.error(f"⚠️ Error connecting to backend: {e}")
