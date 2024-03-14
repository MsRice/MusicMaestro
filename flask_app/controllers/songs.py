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

        if 'new_game' in session:
            session.pop('new_game')
            session.pop('score')

        return render_template("homepage.html", user_info=user_info)
    else:
        return redirect('/')


@app.route('/game_play')
def game_play():
    if is_logged_in():

        user_info = session['user_info']
        if 'new_game' in session:
            x = session['new_game']
            game_of_10 = session['game_of_10']

            count = int(session['score'] / 10)
            x = x + 1

            if x <= 9:
                session['new_game'] = x
            else:
                scores = Song.get_leaderboard()
                data = {
                    'id': user_info['id'],
                    'score': session['score']
                }
                Song.add_score(data)
                session['end_of_game'] = True
                return redirect('/scoreboard')

            response = game_of_10[x]

            quiz = []

            data = {
                'id': response['id']
            }
            quiz = [response]

            fluff = Song.question_fluff(data)
            for answer in fluff:
                quiz.append(answer)
            return render_template('game_wall.html', user_info=user_info,  quiz=quiz, count=count)

        else:
            session['new_game'] = 0
            session['score'] = 0
            session['game_of_10'] = Song.game_of_10()
            game_of_10 = session['game_of_10']

            response = game_of_10[0]

            quiz = []
            data = {
                'id': response['id']
            }
            quiz = [response]

            fluff = Song.question_fluff(data)
            for answer in fluff:
                quiz.append(answer)

            return render_template('game_wall.html', user_info=user_info, game_of_10=game_of_10, quiz=quiz)

    else:
        return redirect('/')


@app.route('/scoreboard')
def scoreboard():
    if is_logged_in():
        user_info = session['user_info']

        scores = Song.get_leaderboard()

        return render_template('scoreboard.html', user_info=user_info, scores=scores)
    else:
        return redirect('/')


@app.route('/song_choice', methods=['POST'])
def song_choice():

    correct = request.form['correct-answer']
    choice = request.form['choice']

    if correct == choice:
        session['score'] = session['score'] + 10

    return redirect('/game_play')
