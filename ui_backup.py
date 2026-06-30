import gradio as gr
import time

from core.chatbot import ask_lumina
from document_reader import read_document
from dashboard import get_session_stats
from flashcards import generate_flashcards, format_flashcards


# -----------------------------
# SESSION STORAGE
# -----------------------------

chat_history = []
question_count = 0
flashcard_count = 0
document_count = 0
session_start = time.time()


# -----------------------------
# MAIN CHAT FUNCTION
# -----------------------------

def chat(message, history, mode, document):

    global question_count
    global document_count

    document_text = ""

    if document is not None:
        try:
            document_text = read_document(document)
            document_count = 1
        except Exception:
            document_text = ""

    reply = ask_lumina(
        user_message=message,
        mode=mode,
        document_text=document_text
    )

    question_count += 1

    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return "", history


# -----------------------------
# FLASHCARD BUTTON
# -----------------------------

def build_flashcards(document):

    global flashcard_count

    if document is None:
        return "Please upload a document first."

    text = read_document(document)

    if not text.strip():
        return "No readable text found."

    cards = generate_flashcards(text)

    flashcard_count = len(cards)

    return format_flashcards(cards)


# -----------------------------
# DASHBOARD
# -----------------------------

def dashboard_text():

    elapsed = int(time.time() - session_start)

    minutes = elapsed // 60
    seconds = elapsed % 60

    stats = get_session_stats(
        {
            "questions": question_count,
            "mode": "",
            "document_loaded": document_count > 0,
            "flashcards": flashcard_count,
            "chat_history": chat_history
        }
    )

    return f"""
## 📊 Dashboard

**Questions Asked:** {stats['questions']}

**Study Time:** {minutes}m {seconds}s

**Documents Uploaded:** {document_count}

**Flashcards Generated:** {flashcard_count}
"""


# -----------------------------
# CSS
# -----------------------------

CUSTOM_CSS = """

.gradio-container{

max-width:1400px !important;

margin:auto;

}

#title{

text-align:center;

font-size:36px;

font-weight:bold;

margin-bottom:15px;

}

#subtitle{

text-align:center;

margin-bottom:25px;

color:gray;

}

"""# ----------------------------------------------------
# BUILD USER INTERFACE
# ----------------------------------------------------

def build_ui():

    with gr.Blocks(
        title="Lumina AI",
        css=CUSTOM_CSS,
        theme=gr.themes.Soft()
    ) as demo:

        gr.Markdown(
            "# 🎓 Lumina AI",
            elem_id="title"
        )

        gr.Markdown(
            "### Your Personal AI Study Assistant",
            elem_id="subtitle"
        )

        with gr.Row():

            # ==========================
            # LEFT SIDEBAR
            # ==========================

            with gr.Column(scale=1):

                mode = gr.Dropdown(
                    choices=[
                        "📘 Explain",
                        "📝 Quiz",
                        "📄 Summarize",
                        "🎯 Exam Prep"
                    ],
                    value="📘 Explain",
                    label="Study Mode"
                )

                upload = gr.File(
                    label="Upload Notes",
                    file_types=[".pdf", ".txt"]
                )

                flashcard_button = gr.Button(
                    "🧠 Generate Flashcards",
                    variant="secondary"
                )

                flashcard_output = gr.Markdown(
                    label="Flashcards"
                )

                dashboard = gr.Markdown(
                    dashboard_text()
                )

                refresh_dashboard = gr.Button(
                    "🔄 Refresh Dashboard"
                )

            # ==========================
            # RIGHT SIDE
            # ==========================

            with gr.Column(scale=3):

                chatbot = gr.Chatbot(
                    height=600,
                    type="messages",
                    label="Conversation"
                )

                user_message = gr.Textbox(
                    placeholder="Ask anything about your studies...",
                    lines=2,
                    label="Your Question"
                )

                with gr.Row():

                    send_button = gr.Button(
                        "Send",
                        variant="primary"
                    )

                    clear_button = gr.Button(
                        "Clear Chat"
                    )        # ==========================================
        # EVENTS
        # ==========================================

        send_button.click(
            fn=chat,
            inputs=[
                user_message,
                chatbot,
                mode,
                upload
            ],
            outputs=[
                user_message,
                chatbot
            ]
        )

        user_message.submit(
            fn=chat,
            inputs=[
                user_message,
                chatbot,
                mode,
                upload
            ],
            outputs=[
                user_message,
                chatbot
            ]
        )

        flashcard_button.click(
            fn=build_flashcards,
            inputs=upload,
            outputs=flashcard_output
        )

        refresh_dashboard.click(
            fn=dashboard_text,
            outputs=dashboard
        )

        clear_button.click(
            lambda: [],
            outputs=chatbot
        )

    return demo