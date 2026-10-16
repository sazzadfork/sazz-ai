
# SAZZ AI - Personal AI Assistant

APP_NAME = "SAZZ AI"

print("=" * 40)
print(f"       Welcome to {APP_NAME}")
print("       Your Personal AI Assistant")
print("=" * 40)

print("\nSAZZ AI: Assalamu Alaikum!")
print("SAZZ AI: Ami tomar personal assistant.")
print("SAZZ AI: Kotha bolte paro. Ber hote 'exit' lekho.\n")

while True:
    question = input("You: ").strip()
    msg = question.lower()

    if msg == "exit":
        print(f"{APP_NAME}: Allah Hafez! Abar kotha hobe.")
        break

    elif "তোমার নাম" in question or "your name" in msg:
        print(f"{APP_NAME}: Amar naam SAZZ AI!")

    elif "কেমন আছ" in question:
        print(f"{APP_NAME}: Ami bhalo achi! Tumi kemon acho?")

    elif "hello" in msg or "hi" == msg:
        print(f"{APP_NAME}: Hello! How can I help you?")

    elif "তোমার কাজ" in question:
        print(f"{APP_NAME}: Ami tomar personal AI assistant.")

    else:
        print(f"{APP_NAME}: Ei proshner uttor dite amake aro shikhte hobe.")
