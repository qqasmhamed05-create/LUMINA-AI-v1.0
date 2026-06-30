from datetime import datetime


def export_chat(history):

    if not history:
        return "No conversation available."

    filename = f"lumina_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=====================================\n")
        file.write("        Lumina AI Chat Export\n")
        file.write("=====================================\n\n")

        for user, assistant in history:

            file.write(f"You:\n{user}\n\n")

            file.write(f"Lumina:\n{assistant}\n\n")

            file.write("-------------------------------------\n\n")

    return filename