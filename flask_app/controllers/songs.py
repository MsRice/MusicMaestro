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
        game_of_10 = Song.game_of_10()

        quiz = []
        for question in game_of_10:
            data = {
                'id': question['id']
            }
            new_question = [question['title']]

            fluff = Song.question_fluff(data)
            for answer in fluff:
                new_question.append(answer['title'])

           # print(new_question)
            quiz.append(new_question)
        return render_template("music_maestro.html", user_info=user_info, game_of_10=game_of_10, quiz=quiz)
    else:
        return redirect('/')
