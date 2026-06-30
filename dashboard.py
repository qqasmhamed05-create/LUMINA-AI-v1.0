import time

# -----------------------------
# GLOBAL SESSION TRACKER
# -----------------------------
SESSION = {
    "questions": 0,
    "mode": "📘 Explain",
    "files_uploaded": 0,
    "flashcards": 0,
    "start_time": time.time(),
    "history": []
}

# -----------------------------
# UPDATE STATS
# -----------------------------
def update_stats(session_data):
    global SESSION

    SESSION["questions"] = session_data.get("questions", SESSION["questions"])
    SESSION["mode"] = session_data.get("mode", SESSION["mode"])
    SESSION["files_uploaded"] = int(session_data.get("document_loaded", False))
    SESSION["flashcards"] = session_data.get("flashcards", SESSION["flashcards"])
    SESSION["history"] = session_data.get("chat_history", SESSION["history"])

# -----------------------------
# GET SESSION STATS
# -----------------------------
def get_session_stats(session_data=None):
    global SESSION

    if session_data:
        update_stats(session_data)

    elapsed = int(time.time() - SESSION["start_time"])
    minutes = elapsed // 60
    seconds = elapsed % 60

    return {
        "questions": SESSION["questions"],
        "mode": SESSION["mode"],
        "document_loaded": bool(SESSION["files_uploaded"]),
        "flashcards": SESSION["flashcards"],
        "time": f"{minutes}m {seconds}s"
    }

# -----------------------------
# RESET SESSION (OPTIONAL)
# -----------------------------
def reset_session():
    global SESSION

    SESSION = {
        "questions": 0,
        "mode": "📘 Explain",
        "files_uploaded": 0,
        "flashcards": 0,
        "start_time": time.time(),
        "history": []
    }