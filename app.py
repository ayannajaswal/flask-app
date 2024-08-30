from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for messages
messages = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'GET':
        return jsonify(messages)

    if request.method == 'POST':
        data = request.json
        sender_id = data.get('sender_id')
        message = data.get('message')

        if sender_id and message:
            messages.setdefault(sender_id, []).append(message)
            return jsonify({"status": "Message received"}), 201
        return jsonify({"error": "Invalid data"}), 400

@app.route('/messages/<sender_id>', methods=['GET'])
def get_messages(sender_id):
    return jsonify(messages.get(sender_id, []))

if __name__ == '__main__':
    app.run(debug=True)
