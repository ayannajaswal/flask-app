document.addEventListener('DOMContentLoaded', () => {
    const messagesContainer = document.getElementById('messages');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    function fetchMessages() {
        fetch('/messages')
            .then(response => response.json())
            .then(data => {
                messagesContainer.innerHTML = '';
                for (const [sender, msgs] of Object.entries(data)) {
                    msgs.forEach(msg => {
                        const msgElement = document.createElement('div');
                        msgElement.textContent = `${sender}: ${msg}`;
                        messagesContainer.appendChild(msgElement);
                    });
                }
            });
    }

    function sendMessage() {
        const message = messageInput.value;
        if (message) {
            fetch('/messages', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    sender_id: 'User1',  // Replace 'User1' with the actual sender ID
                    message: message
                }),
            })
            .then(response => {
                if (response.status === 201) {
                    messageInput.value = '';
                    fetchMessages();  // Refresh messages after sending
                }
            })
            .catch(error => console.error('Error sending message:', error));
        }
    }

    // Add event listener to send button
    sendButton.addEventListener('click', sendMessage);

    // Optional: Fetch messages initially when the page loads
    fetchMessages();
});
