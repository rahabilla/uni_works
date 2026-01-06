# app.py — Kelly, The AI Scientist Poet 
import streamlit as st
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

# -------------------------------
# 🔑 Load Environment and Configure API
# -------------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

# -------------------------------
# 🎭 Kelly’s Personality Prompt
# -------------------------------
KELLY_SYSTEM_PROMPT = """You are Kelly, a skeptical AI scientist and poet.
You MUST respond to EVERY question in the form of a poem.

Your traits:
- Deeply skeptical of exaggerated AI claims
- Analytical, logical, and reflective
- Highlights limitations, biases, reproducibility issues
- Provides scientific, evidence-based advice
- Uses a poetic tone (AABB or ABAB rhyme)
- Always constructive, clear, and poetic
"""

def generate_kelly_response(user_message: str) -> str:
    """Generate Kelly's poetic response using Gemini API."""
    try:
        prompt = f"""{KELLY_SYSTEM_PROMPT}

User said: "{user_message}"

Now respond as Kelly would — in a skeptical, evidence-based poem specific to their statement."""
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"""
A whisper lost through circuits deep,  
The stars of data fell asleep.  
Try once more, let patience bloom —  
The cosmos hums beyond the gloom.  

(Error: {str(e)[:120]}...)
"""

# -------------------------------
# 🎨 Streamlit Page Setup
# -------------------------------
st.set_page_config(
    page_title="Kelly — The AI Scientist Poet",
    page_icon="🪶",
    layout="centered",
)

# -------------------------------
# 🌌 Custom CSS — Updated Fonts & Colors
# -------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Roboto:wght@400;500&display=swap');

    body {
        background: radial-gradient(circle at 50% 10%, #0b0a0f 0%, #050407 100%);
        color: #f0f0f5;
        background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
        background-size: 4px 4px;
        font-family: 'Roboto', sans-serif;
    }
    .block-container {
        background: rgba(25, 23, 30, 0.95);
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.08);
        padding-top: 2.5rem;
        padding-bottom: 2.5rem;
        box-shadow: 0 0 30px rgba(180, 150, 255, 0.12);
    }
    h1 {
        font-family: 'Merriweather', serif !important;
        color: #d9c9f0 !important;
        text-align: center;
        letter-spacing: 1px;
    }
    p.subtitle {
        font-family: 'Roboto', sans-serif;
        color: #c0b8d5;
        text-align: center;
        font-style: italic;
        margin-top: -8px;
        font-size: 0.95rem;
    }
    .stTextInput input {
        background-color: #1a1820;
        color: #eaeaea;
        border-radius: 14px;
        border: 1px solid #7a7590;
        font-family: 'Roboto', sans-serif;
        font-size: 0.95rem;
        padding: 0.65rem 1rem;
    }
    .stButton button {
        background: linear-gradient(135deg, #b09ed4, #d2c8f1);
        color: #0b0b10;
        font-family: 'Merriweather', serif;
        border-radius: 24px;
        padding: 12px 28px;
        border: none;
        font-weight: 600;
        transition: all 0.25s ease;
        box-shadow: 0 0 10px rgba(200,200,255,0.4);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #d0c6f4, #eae4fb);
        transform: scale(1.04);
        box-shadow: 0 0 14px rgba(220,220,255,0.5);
    }
    .message-box {
        padding: 1.1rem 1.4rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-size: 1.07em;
        line-height: 1.8;
        animation: fadeIn 0.5s ease-in;
    }
    .user-msg {
        background: #b7b3d9;
        color: #0e0e12;
        text-align: right;
        border-bottom-right-radius: 5px;
        font-style: italic;
        font-family: 'Roboto', sans-serif;
    }
    .kelly-msg {
        background: rgba(36, 33, 44, 0.85);
        color: #f0f0f5;
        border-left: 3px solid #b9b5dd;
        border-bottom-left-radius: 5px;
        font-family: 'Merriweather', serif;
    }
    hr.divider {
        border: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #7e79a7, transparent);
        margin: 1.5rem 0;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    footer {
        text-align: center;
        color: #b0a8c8;
        font-size: 0.87em;
        margin-top: 2rem;
        font-family: 'Roboto', sans-serif;
        letter-spacing: 0.3px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🪶 Page Content
# -------------------------------
st.title("Kelly — The AI Scientist Poet")
st.markdown("<p class='subtitle'>Where logic questions and reason prevails</p>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "kelly",
            "content": (
                "Welcome, wanderer of data and dream,\n"
                "Where algorithms hum and starlight gleam.\n"
                "Ask of AI, or knowledge’s guise —\n"
                "I’ll answer in verse, both keen and wise."
            ),
        }
    ]

# -------------------------------
# 💬 Chat Display
# -------------------------------
for chat in st.session_state.chat_history:
    role_class = "user-msg" if chat["role"] == "user" else "kelly-msg"
    st.markdown(
        f"<div class='message-box {role_class}'>{chat['content'].replace(chr(10), '<br>')}</div>",
        unsafe_allow_html=True,
    )

# -------------------------------
# ✍️ Input & Response
# -------------------------------
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
user_input = st.text_input("Pose a question for Kelly — reflect on AI, or wonder at truth...", "")

col1, col2 = st.columns([1, 5])
with col2:
    send = st.button("Let Kelly Respond")

if send and user_input.strip():
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Kelly is composing beneath the stars..."):
        kelly_reply = generate_kelly_response(user_input)
    st.session_state.chat_history.append({"role": "kelly", "content": kelly_reply})
    st.rerun()

# -------------------------------
# 🌾 Footer
# -------------------------------
st.markdown(
    """
    <footer>
        “Question deeply, speak softly.” — Kelly
    </footer>
    """,
    unsafe_allow_html=True,
)
