
from flask import Flask, render_template, request

app = Flask(__name__)

def get_reply(message):
    question = message.lower().strip()

    if "তোমার নাম" in question or "your name" in question:
        return "আমার নাম SAZZ AI! আমি তোমার Personal AI Assistant."

    if "কেমন আছ" in question:
        return "আমি ভালো আছি! 😊 তুমি কেমন আছ?"

    if "হ্যালো" in question or "সালাম" in question:
        return "আসসালামু আলাইকুম! আমি SAZZ AI। কীভাবে সাহায্য করব?"

    if "hello" in question or question == "hi":
        return "Hello! I am SAZZ AI. How can I help you?"

    return "তোমার প্রশ্নটি পেয়েছি! আসল AI Brain যুক্ত করলে আমি আরও বুদ্ধিমান উত্তর দিতে পারব।"

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form.get("message", "").strip()

        if user_message:
            reply = get_reply(user_message)

    return render_template(
        "index.html",
        reply=reply,
        user_message=user_message
    )

if __name__ == "__main__":
    app.run(debug=True)
