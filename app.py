from flask import Flask, render_template, redirect, url_for, sessions
from flask_session import Session


app = Flask(__name__)

@app.route('/')
def homepage():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/playlists')
def playlists():
    pass

@app.route('/your-music')
def songs():
    pass

@app.route('/settings')
def settings():
   pass

@app.route('/register')
def register():
    pass






if __name__ == '__main__':
    app.run()