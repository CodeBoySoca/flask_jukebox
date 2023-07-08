from flask import Flask, render_template, redirect, url_for, session, request
from flask_session import Session

app = Flask(__name__)
Session(app)

@app.route('/')
def homepage():
    return render_template('index.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form.to_dict()
    return render_template('login.j2')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form.to_dict()
    return render_template('register.j2')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/playlists', methods=['GET', 'POST'])
def playlists():
    if request.method == 'POST':
       form = request.form.to_dict()
    return render_template('playlists.j2')

@app.route('/your-music',  methods=['GET', 'POST'])
def songs():
    if request.method == 'POST':
        form = request.form.to_dict()
    return render_template('music.j2')

@app.route('/settings')
def settings():
   return render_template('settings.j2')

@app.route('/email/registration')
def email():
    pass

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.j2')

if __name__ == '__main__':
    app.run(port=5111)