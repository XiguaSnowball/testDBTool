from testDBTool import app
from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g


@app.route('/login', methods=['POST'])
def show_results():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('results'))


@app.route('/register', methods=['POST'])
def show_results():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('results'))


@app.route('/results', methods=['POST'])
def show_results():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('results'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=request.form['username']).first()
        passwd = User.query.filter_by(password=request.form['password']).first()

        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))
