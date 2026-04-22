import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(
    page_title="MediScan AI Malaysia",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 MediScan AI Malaysia")
st.subheader("AI-Powered Medical Image Analysis for Rural Healthcare Workers")
st.markdown("---")

api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

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
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = """You are an AI medical assistant helping rural healthcare workers in Malaysia.
            Analyze this medical image and provide:
            1. What you observe in the image
            2. Possible conditions or findings
            3. Recommended next steps
            4. When to refer to a specialist
            
            Important: This is for educational assistance only. Always consult a qualified doctor."""
            
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            response = model.generate_content([
                prompt,
                {"mime_type": "image/png", "data": img_byte_arr}
            ])
            
            st.markdown("### 🤖 AI Analysis Result")
            st.success(response.text)
            st.warning("⚠️ This is AI-assisted analysis for educational purposes only. Always consult a qualified medical professional.")

elif uploaded_file and not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar.")

st.markdown("---")
st.markdown("**MediScan AI Malaysia** | MyAI Future Hackathon 2026 | Healthcare Track")
st.markdown("Built with Google Gemini API + Streamlit | by Hafiz Kamar")
