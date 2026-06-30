
import gradio as gr
from core.chatbot import ask_lumina
from document_reader import read_document

session = []

CSS = """
#title{text-align:center;font-size:34px;font-weight:bold;color:#1d4ed8}
#subtitle{text-align:center;color:#666;margin-bottom:12px}
footer{display:none!important}
"""

def respond(message, history, mode, file):
    doc_text = ""
    if file is not None:
        try:
            doc_text = read_document(file)
        except Exception:
            doc_text = ""

    reply = ask_lumina(message, mode, doc_text)

    history = history or []
    history.append({"role":"user","content":message})
    history.append({"role":"assistant","content":reply})
    return history, "", history

with gr.Blocks() as demo:
    gr.Markdown("# 🎓 Lumina AI", elem_id="title")
    gr.Markdown("### Your Personal AI Study Assistant", elem_id="subtitle")

    with gr.Row():
        with gr.Column(scale=1):
            mode = gr.Dropdown(
                ["📘 Explain","📝 Quiz","📄 Summarize","🎯 Exam Prep"],
                value="📘 Explain",
                label="Study Mode"
            )
            upload = gr.File(
                label="Upload PDF / TXT",
                file_types=[".pdf",".txt"]
            )
            clear = gr.Button("🗑️ Clear Chat", variant="secondary")

        with gr.Column(scale=4):
            chatbot = gr.Chatbot(height=550)
            msg = gr.Textbox(
                placeholder="Ask anything about your studies...",
                label="Message"
            )
            send = gr.Button("Send", variant="primary")

    state = gr.State([])

    send.click(
        respond,
        inputs=[msg, state, mode, upload],
        outputs=[chatbot, msg, state]
    )

    msg.submit(
        respond,
        inputs=[msg, state, mode, upload],
        outputs=[chatbot, msg, state]
    )

    clear.click(
        lambda: ([], "", []),
        outputs=[chatbot, msg, state]
    )

if __name__ == "__main__":
    demo.launch(
    css=CSS,
    theme=gr.themes.Soft()
)
