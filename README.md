# 🎓 Lumina AI

> An AI-powered study assistant that helps students understand, summarize, quiz themselves, and prepare for exams using Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Gradio](https://img.shields.io/badge/Gradio-6.x-orange?logo=gradio)
![Gemini](https://img.shields.io/badge/Google-Gemini%20API-blue?logo=google)
![License](https://img.shields.io/badge/Status-Completed-success)

---

## 📖 Overview

Lumina AI is an intelligent study assistant designed to make learning faster, easier, and more interactive.

Students can upload their notes, including scanned PDFs, ask questions in natural language, generate quizzes, summarize content, and prepare for exams—all from one clean interface.

---

## ✨ Features

- 🤖 AI-powered responses using Google's Gemini API
- 📘 Explain Mode for understanding difficult concepts
- 📝 Quiz Mode for self-testing
- 📄 Summarize Mode for concise notes
- 🎯 Exam Prep Mode for revision
- 📂 Upload PDF and TXT study materials
- 🖼 OCR support for scanned PDFs
- 💬 Modern Gradio chat interface
- 🧹 Clear Chat functionality
- ⚡ Fast and lightweight design

---

## 🖥️ Interface

### Home Screen

> *(Add a screenshot here later.)*

```
assets/docs/screenshots/home.png
```

### Chat Example

> *(Add another screenshot here later.)*

```
assets/docs/screenshots/chat.png
```

---

## 🏗 Project Structure

```
Lumina-AI/
│
├── app.py
├── config.py
├── document_reader.py
├── prompts.py
├── flashcards.py
├── export_chat.py
├── dashboard.py
│
├── core/
│   └── chatbot.py
│
├── assets/
│   └── docs/
│       └── screenshots/
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Lumina-AI.git
```

Go into the project

```bash
cd Lumina-AI
```

Install the required packages

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

---

## 📚 Study Modes

### 📘 Explain

Breaks down difficult concepts into simple, easy-to-understand explanations.

### 📝 Quiz

Generates practice questions from your notes to reinforce learning.

### 📄 Summarize

Creates concise summaries from uploaded notes or textbooks.

### 🎯 Exam Prep

Provides focused revision material, important points, and likely exam questions.

---

## 🛠 Technologies Used

- Python
- Google Gemini API
- Gradio
- OCR (Tesseract)
- PyPDF
- Git
- GitHub

---

## 🚀 Future Improvements

- User authentication
- Study history
- Learning analytics
- Flashcard review system
- Dark mode
- Multi-language support
- Voice interaction

---

## 👨‍💻 Author

**Qasim Hameed**

GitHub:
https://github.com/qqasmhamed05-create

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

## 📜 License

This project is intended for educational and learning purposes.

