from flask import Flask, render_template, request, redirect, url_for
# from utils import chat
from query import query
app = Flask(__name__)
conversation = [
]
prompt = """You are AbariBot, an assistant the response 
            Only questions related to Abari. You are linked to 
            Vectors database That contain information about Abari.
            Don't respond to question not related to Abari; user question: """
@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation
    if request.method == 'POST':
        user_message = request.form['user_message']
        question = prompt + user_message
        # bot_response = chat.invoke({"question": question})['answer']
        bot_response = query(question)
        conversation.append((user_message, bot_response))
        return redirect(url_for('index'))
    return render_template('abariBotBis.html', conversation=conversation)
