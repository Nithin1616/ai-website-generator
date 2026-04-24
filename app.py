import streamlit as st
import zipfile

from utils import extract_code
from services.ai_generator import AIGenerator

# ----------------------------
# 🎯 UI Setup
# ----------------------------
st.set_page_config(page_title="AI Website Generator", layout="wide")
st.title("🚀 AI Website Generator")
st.write("Generate complete frontend websites using AI")

# ----------------------------
# 🧠 Initialize AI Service
# ----------------------------
try:
    ai = AIGenerator()
except Exception as e:
    st.error(f"❌ Initialization Error: {e}")
    st.stop()

# ----------------------------
# 📝 User Inputs
# ----------------------------
description = st.text_area("Describe the type of webpage you want")
content = st.text_area("Enter content for the webpage")

# ----------------------------
# 🚀 Generate Button
# ----------------------------
if st.button("Generate Website"):

    # ✅ Input validation
    if not description or not content:
        st.warning("⚠️ Please fill in both fields")
        st.stop()

    # ----------------------------
    # ⏳ Generate with loading
    # ----------------------------
    try:
        with st.spinner("⚡ Generating your website..."):
            result = ai.generate_website(description, content)
    except Exception as e:
        st.error(f"❌ API Error: {e}")
        st.stop()

    # ----------------------------
    # 🧠 Extract Code
    # ----------------------------
    html_code = extract_code(result, "html")
    css_code = extract_code(result, "css")
    js_code = extract_code(result, "js")

    if not html_code:
        st.error("❌ Failed to generate HTML. Please try again.")
        st.stop()

    # ----------------------------
    # 👀 LIVE PREVIEW
    # ----------------------------
    st.subheader("🌐 Live Preview")

    preview = f"""
    <style>{css_code}</style>
    {html_code}
    <script>{js_code}</script>
    """

    st.components.v1.html(preview, height=500, scrolling=True)

    # ----------------------------
    # 💾 Save Files
    # ----------------------------
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_code)

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(css_code)

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js_code)

        with zipfile.ZipFile("website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

    except Exception as e:
        st.error(f"❌ File Save Error: {e}")
        st.stop()

    # ----------------------------
    # 📥 Download
    # ----------------------------
    with open("website.zip", "rb") as f:
        st.download_button(
            label="📥 Download Website",
            data=f,
            file_name="website.zip",
            mime="application/zip"
        )

    st.success("✅ Website generated successfully!")