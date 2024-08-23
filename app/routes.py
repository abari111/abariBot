from flask import Flask, render_template, request, redirect, url_for
from utils import chat

app = Flask(__name__)
conversation = [
]


@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation
    if request.method == 'POST':
        user_message = request.form['user_message']
        bot_response = chat.invoke({"question": user_message})['answer']
        conversation.append((user_message, bot_response))
        return redirect(url_for('index'))
    return render_template('abariBot.html', conversation=conversation)
