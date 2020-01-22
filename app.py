from flask import Flask, render_template

app = Flask(__name__)
@app.route('/<nick>')
def index(nick):
    return "Hello " + nick;
