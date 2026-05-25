import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# =========================================================
# OPENROUTER API KEY
# =========================================================

API_KEY = st.secrets.get("OPENROUTER_API_KEY") or st.secrets["OPENROUTER_API_KEY"]


# =========================================================
# GENERATE SYLLABUS FUNCTION
# =========================================================

def generate_syllabus(topic, task):

    prompt = f"""
You are an AI teacher.

Create a beginner-friendly syllabus for the topic below.

Topic:
{topic}

Task:
{task}

Instructions:
- Create step-by-step learning modules
- Keep it concise
- Use bullet points
- Beginner friendly
"""

    try:

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },

            json={
                "model": "openrouter/free",

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                "temperature": 0.7,
                "max_tokens": 800
            },

            timeout=60
        )

        result = response.json()

        print(result)

        if "choices" not in result:

            return f"API Error: {result}"

        syllabus = result["choices"][0]["message"]["content"]

        return syllabus

    except Exception as e:

        return f"Error: {str(e)}"