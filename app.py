import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io
import os

st.set_page_config(page_title="MediScan AI Malaysia", page_icon="🏥", layout="centered")
st.title("🏥 MediScan AI Malaysia")
st.subheader("AI-Powered Medical Image Analysis for Rural Healthcare Workers")
st.markdown("---")

# Get API key from secrets or sidebar
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

st.markdown("### Upload a Medical Image")
uploaded_file = st.file_uploader("Upload an X-ray, skin condition, or wound image", type=["jpg", "jpeg", "png"])

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing with Gemini AI..."):
            try:
                client = genai.Client(api_key=api_key)
                
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_bytes = img_byte_arr.getvalue()

                prompt = """You are an AI medical assistant helping rural healthcare workers in Malaysia.
                Analyze this medical image and provide:
                1. What you observe in the image
                2. Possible conditions or findings
                3. Recommended next steps
                4. When to refer to a specialist
                Important: This is for educational assistance only."""

                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=[
                        prompt,
                        types.Part.from_bytes(data=img_bytes, mime_type="image/png")
                    ]
                )

                st.markdown("### 🤖 AI Analysis Result")
                st.success(response.text)
                st.warning("⚠️ For educational purposes only. Always consult a qualified doctor.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

elif uploaded_file and not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar.")

st.markdown("---")
st.markdown("**MediScan AI Malaysia** | MyAI Future Hackathon 2026 | Healthcare Track")
st.markdown("Built with Google Gemini API + Streamlit | by Hafiz Kamar")
