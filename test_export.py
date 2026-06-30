from export_chat import export_chat

history = [
    ("What is photosynthesis?", "Photosynthesis is the process by which plants make food."),
    ("When did WW1 begin?", "World War I began in 1914.")
]

filename = export_chat(history)

print(filename)