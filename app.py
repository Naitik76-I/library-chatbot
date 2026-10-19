from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rule-based chatbot logic function
def get_bot_response(user_input):
    user_input = user_input.strip().lower()
    
    if 'time' in user_input or 'hours' in user_input or 'open' in user_input:
        return "Our library is open Monday to Saturday from 9:00 AM to 8:00 PM. We are closed on Sundays."
    elif 'membership' in user_input or 'card' in user_input or 'join' in user_input:
        return "To get a library card, please visit the front desk with a valid photo ID and proof of address. Membership is free!"
    elif 'fine' in user_input or 'late' in user_input:
        return "Late fines are $0.50 per book, per day."
    elif 'book' in user_input or 'search' in user_input or 'catalog' in user_input:
        return "You can browse our full collection online at citylibrary.org/catalog."
    elif 'help' in user_input:
        return "You can ask me about library timings, memberships, late fines, or book catalogs!"
    else:
        return "I'm sorry, I didn't quite catch that. Type 'help' for assistance!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("msg", "")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)