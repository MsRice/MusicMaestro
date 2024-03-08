from flask import Flask
app = Flask(__name__)
app.secret_key = "its@secret"  # bad practice always encrypt passwords!!!
