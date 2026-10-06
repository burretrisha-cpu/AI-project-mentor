import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Project Mentor",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Gemini API Setup
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Project Mentor")
st.write(
    "Your intelligent guide for choosing, planning, and developing academic projects."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("📌 Project Details")

branch = st.sidebar.selectbox(
    "Select Branch",
    ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil", "Other"]
)

year = st.sidebar.selectbox(
    "Select Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

level = st.sidebar.selectbox(
    "Project Level",
    ["Beginner", "Intermediate", "Advanced"]
)

domain = st.sidebar.selectbox(
    "Project Domain",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Web Development",
        "Data Science",
        "Cyber Security",
        "IoT",
        "Cloud Computing",
        "Other"
    ]
)

# -----------------------------
# Main Input
# -----------------------------
st.subheader("💡 Tell Me About Your Project")

project_idea = st.text_area(
    "Enter your project idea",
    placeholder="Example: I want to create an AI chatbot for students..."
)

goal = st.text_area(
    "What do you want your project to achieve?",
    placeholder="Example: Help students get answers to their academic questions."
)

# -----------------------------
# AI Mentor Function
# -----------------------------
def get_ai_response(prompt):

    if not client:
        return "⚠️ Gemini API key not found. Please add GEMINI_API_KEY to your .env file."

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"


# -----------------------------
# Generate Mentor Advice
# -----------------------------
if st.button("🚀 Get Mentor Guidance", use_container_width=True):

    if not project_idea.strip():
        st.warning("Please enter your project idea first.")

    else:

        prompt = f"""
You are an AI Project Mentor helping college students.

Student Details:
Branch: {branch}
Year: {year}
Project Level: {level}
Domain: {domain}

Project Idea:
{project_idea}

Project Goal:
{goal}

Analyze the student's idea and provide useful project guidance.

Give the response in this format:

1. Project Title
2. Project Overview
3. Problem Statement
4. Objectives
5. Recommended Technologies
6. Main Modules
7. How the System Works
8. Development Roadmap
9. Expected Output
10. Future Enhancements

Keep the explanation simple and suitable for a college student.
Suggest realistic technologies and features that can actually be implemented.
"""

        with st.spinner("🤖 AI Mentor is analyzing your project..."):
            answer = get_ai_response(prompt)

        st.subheader("🎯 AI Mentor's Guidance")
        st.markdown(answer)


# -----------------------------
# Project Planning Section
# -----------------------------
st.divider()

st.subheader("🛠️ What Can AI Project Mentor Help With?")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "💡 **Project Ideas**\n\n"
        "Get project ideas based on your branch, year and interests."
    )

with col2:
    st.info(
        "🗺️ **Project Roadmap**\n\n"
        "Get step-by-step guidance for developing your project."
    )

with col3:
    st.info(
        "💻 **Technology Selection**\n\n"
        "Choose suitable programming languages, frameworks and tools."
    )

st.divider()

st.caption("AI Project Mentor | Academic Project Guidance System")