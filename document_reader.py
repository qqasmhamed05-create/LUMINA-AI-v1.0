from pypdf import PdfReader


def read_document(file):
    if file is None:
        return ""

    filename = file.name.lower()

    if filename.endswith(".txt"):
        with open(file.name, "r", encoding="utf-8") as f:
            return f.read()

    elif filename.endswith(".pdf"):
        reader = PdfReader(file.name)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    return ""