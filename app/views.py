from . import app
from .database import test_create, select_user, test_select_all, reg_user
from .forms import RegForm, LoginForm
from .models import login_required

from flask import render_template, request, redirect, url_for, flash, session, jsonify

@app.before_first_request
def setup():
    test_create()
    print('DATABASE CREATED')

@app.route('/')
def index():
    data_all = test_select_all()
    print('DATA ALL:', data_all)
    data = select_user("admin")
    print('DATA SELECT:', data)
    return render_template('index.html', data = data, data_all = data_all)

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
    form = RegForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        try:
            reg_user(username, password)
            flash('Successful registration!', 'success')
            return redirect(url_for('index'))
        except:
            flash('Something went wrong')
            return redirect(url_for('reg_user'))

    return render_template('reg.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        entered_password = form.password.data

        data = select_user(username)
        if data:
            actual_password = data[0][1]
            if entered_password == actual_password:
                session['logged_in'] = True
                session['username'] = username
                flash('Logged in!', 'success')
                return redirect(url_for('index'))
            else:   
                error = 'Invalid username or password'
                return render_template('login.html', error=error, form=form)
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/general', methods = ['GET', 'POST'])
def general():
    messages = []

    req = request.get_json()
    print(req)

    return render_template('general_chat.html')