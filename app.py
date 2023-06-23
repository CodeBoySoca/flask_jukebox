from flask import Flask, render_template, redirect, url_for, session
from flask_session import Session


app = Flask(__name__)
Session(app)

@app.route('/')
def homepage():
    return render_template('index.j2')

@app.route('/login')
def login():
    return render_template('login.j2')

@app.route('/register')
def register():
    return render_template('register.j2')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/playlists')
def playlists():
    return render_template('playlists.j2')

@app.route('/your-music')
def songs():
    return render_template('music.j2')

@app.route('/settings')
def settings():
   return render_template('settings.j2')

@app.route('/email/registration')
def email():
    pass






if __name__ == '__main__':
    app.run()