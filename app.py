from flask import Flask, render_template

app = Flask(__name__)
chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
