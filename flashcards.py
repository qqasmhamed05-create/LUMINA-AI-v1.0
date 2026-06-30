import re

# -----------------------------
# KEYWORD EXTRACTION (offline AI-like logic)
# -----------------------------
def extract_key_points(text, limit=10):

    # split sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # remove very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    # prioritize sentences with important keywords
    keywords = [
        "because", "therefore", "as a result", "important",
        "caused", "led to", "effect", "impact", "reason",
        "war", "treaty", "government", "revolution", "economic"
    ]

    scored = []

    for s in sentences:
        score = 0

        for k in keywords:
            if k in s.lower():
                score += 2

        # prefer medium-length sentences
        if 50 <= len(s) <= 200:
            score += 1

        scored.append((score, s))

    # sort by score
    scored.sort(reverse=True, key=lambda x: x[0])

    return [s for _, s in scored[:limit]]


# -----------------------------
# FLASHCARD GENERATOR
# -----------------------------
def generate_flashcards(text, count=10):

    key_points = extract_key_points(text, limit=count)

    flashcards = []

    for point in key_points:

        # simple question generation
        question = create_question(point)
        answer = point

        flashcards.append({
            "front": question,
            "back": answer
        })

    return flashcards


# -----------------------------
# SIMPLE QUESTION CREATOR
# -----------------------------
def create_question(sentence):

    sentence = sentence.strip()

    # rule-based transformations
    if "because" in sentence.lower():
        return "Why is this important?"

    if "led to" in sentence.lower():
        return "What did this lead to?"

    if "effect" in sentence.lower():
        return "What is the effect mentioned?"

    if "war" in sentence.lower():
        return "What is described about the war?"

    # default fallback
    return "Explain this statement in simple terms"


# -----------------------------
# FORMAT FOR DISPLAY
# -----------------------------
def format_flashcards(cards):

    output = ""

    for i, card in enumerate(cards, 1):
        output += f"""
Flashcard {i}
-----------------
Q: {card['front']}
A: {card['back']}

"""

    return output


# -----------------------------
# EXPORT READY FORMAT
# -----------------------------
def export_flashcards(cards):

    text = "LUMINA AI FLASHCARDS\n\n"

    for i, card in enumerate(cards, 1):
        text += f"{i}. Q: {card['front']}\n   A: {card['back']}\n\n"

    return text