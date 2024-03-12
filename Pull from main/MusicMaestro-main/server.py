from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import messages
from flask_app.controllers import songs

if __name__ == '__main__':
    app.run(debug=True)
