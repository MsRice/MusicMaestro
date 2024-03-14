from flask_app import app

from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app.models.user import User
from flask_app.models.song import Song

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/register', methods=["POST"])
def register():
    if not User.registration_validation(request.form):
        session['alert_type'] = 'registration'
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    User.register(data)
    session['alert_type'] = 'registration'
    flash("Successful Registration, Log In!")

    return redirect('/')


@app.route('/login', methods=["POST"])
def login():
    data = {
        'email': request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        session['alert_type'] = 'login'
        flash("Invalid Email")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        session['alert_type'] = 'login'
        flash("Invalid Password")
        return redirect('/')

    user_info = {
        'id': user_in_db.id,
        'first_name': user_in_db.first_name
    }

    session['user_info'] = user_info

    if is_logged_in():
        return redirect('/music_maestro')


@app.route('/is_logged_in')
def is_logged_in():

    is_Logged = False
    print("is_log", is_Logged)

    if 'user_info' in session:
        is_Logged = True
        return is_Logged
    else:
        session['alert_type'] = 'login'
        flash("Must Log In! ")
        is_Logged = False
        return is_Logged


@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect('/')
