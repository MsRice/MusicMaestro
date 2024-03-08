from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.message import Message
from flask_app.models.song import Song
from flask_app.models.user import User

from flask_app.controllers.users import is_logged_in


@app.route('/music_maestro')
def song_wall():
    if is_logged_in():
        user_info = session['user_info']

        return render_template("music_maestro.html", user_info=user_info)
    else:
        return redirect('/')
