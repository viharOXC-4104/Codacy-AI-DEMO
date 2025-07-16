from flask import Flask

from app import routes

app = Flask(__name__)
app.secret_key = 'supersecretkey'
