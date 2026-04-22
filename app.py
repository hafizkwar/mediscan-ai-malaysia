import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import base64

st.set_page_config(
    page_title="MediScan AI Malaysia",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 MediScan AI Malaysia")
st.subheader("AI-Powered Medical Image Analysis for Rural Healthcare Workers")
st.markdown("---")

api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

st.markdown("### Upload a Medical Image")
uploaded_file = st.file_uploader(
    "Upload an X-ray, skin condition, or wound image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing with Gemini AI..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.0-flash-exp")
                
                prompt = """You are an AI medical assistant helping rural healthcare workers in Malaysia.
                Analyze this medical image and provide:
                1. What you observe in the image
                2. Possible conditions or findings
                3. Recommended next steps
                4. When to refer to a specialist
                Important: This is for educational assistance only."""
                
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_bytes = img_byte_arr.getvalue()
                img_b64 = base64.b64encode(img_bytes).decode()
                
                response = model.generate_content([
                    {"role": "user", "parts": [
                        {"text": prompt},
                        {"inline_data": {"mime_type": "image/png", "data": img_b64}}
                    ]}
                ])
                
                st.markdown("### 🤖 AI Analysis Result")
                st.success(response.text)
                st.warning("⚠️ For educational purposes only. Always consult a qualified doctor.")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("💡 Try: 1) Check your API key 2) Wait 1 minute 3) Try a different Google account")

elif uploaded_file and not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar.")

st.markdown("---")
st.markdown("**MediScan AI Malaysia** | MyAI Future Hackathon 2026 | Healthcare Track")
st.markdown("Built with Google Gemini API + Streamlit | by Hafiz Kamar")
