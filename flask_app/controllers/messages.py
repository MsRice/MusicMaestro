from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.message import Message
from flask_app.models.song import Song
from flask_app.models.user import User


@app.route('/messages', methods=['POST'])
def messages():
    print(request.form)
    data = {
        'id': request.form['id'],
        'comment': request.form['comment']
    }
    Message.post_msg(data)

    return redirect('/scoreboard')
