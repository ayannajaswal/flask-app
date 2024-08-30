from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# Define a route to serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('index.html', 'index.html')

# Define a route to serve the CSS file
@app.route('/style.css')
def serve_css():
    return send_from_directory('styles.css', 'style.css')

# Define a route to serve the JavaScript file
@app.route('/script.js')
def serve_js():
    return send_from_directory('script.js', 'script.js')

# Define a route for handling messages
@app.route('/messages', methods=['GET', 'POST'])
def message_handler():
    if request.method == 'POST':
        data = request.json
        sender_id = data.get('sender_id')
        message = data.get('message')

        if sender_id and message:
            if sender_id not in messages:
                messages[sender_id] = []
            messages[sender_id].append(message)
            return '', 201  # 201 Created
        return '', 400  # Bad request
    else:
        return jsonify(messages)

if __name__ == '__main__':
    # Use environment variables for host and port if available
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host=host, port=port, debug=True)
