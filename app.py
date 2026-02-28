import streamlit as st
import PyPDF2
from groq import Groq
import time

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🚀", layout="wide")

# ----------- STYLING -------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #1e3c72, #2a5298, #ff512f, #dd2476);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

h1 {
    text-align: center;
    color: white;
    font-size: 50px;
}

.stButton>button {
    background: linear-gradient(to right, #ff512f, #dd2476);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)

# ----------- TITLE -------------
st.markdown("<h1>🚀 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:white;font-size:18px;'>Smart AI Feedback for Your Career Growth</p>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📄 Upload Resume (PDF or TXT)", type=["pdf","txt"])

if uploaded_file:

    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

    else:
        resume_text = uploaded_file.read().decode("utf-8")

    if st.button("✨ Analyze Resume"):
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        # ----- GROQ API -----
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a professional resume reviewer. Give score out of 100 and improvement suggestions."},
                {"role": "user", "content": resume_text}
            ],
            temperature=0.7,
        )

        result = chat_completion.choices[0].message.content

        st.success("✅ Analysis Complete!")

        # --------- SCORE DISPLAY ----------
        score = 85  # you can later extract dynamically
        st.metric("Resume Score", f"{score}/100")

        st.markdown("### 📊 AI Feedback")
        st.write(result)

        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )

st.markdown("</div>", unsafe_allow_html=True)