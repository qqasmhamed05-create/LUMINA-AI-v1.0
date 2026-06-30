from google import genai
from config import GEMINI_API_KEY
from prompts import (
    BASE_PROMPT,
    EXPLAIN_MODE,
    QUIZ_MODE,
    SUMMARY_MODE,
    EXAM_MODE,
)

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_lumina(user_message, mode, document_text=""):

    if mode == "📘 Explain":
        mode_prompt = EXPLAIN_MODE
    elif mode == "📝 Quiz":
        mode_prompt = QUIZ_MODE
    elif mode == "📄 Summarize":
        mode_prompt = SUMMARY_MODE
    elif mode == "🎯 Exam Prep":
        mode_prompt = EXAM_MODE
    else:
        mode_prompt = EXPLAIN_MODE

    full_prompt = f"""
{BASE_PROMPT}

{mode_prompt}

Student Question:
{user_message}
"""

    if document_text:
        full_prompt += f"""

Uploaded Notes:
{document_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )
        return response.text

    except Exception as e:
        return f"⚠️ AI Error:\n{str(e)}"