from flask import redirect, url_for, flash, session

# Login required decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('Access denied, please log in', 'danger')
            return redirect(url_for('login'))
    wrapper.__name__ = func.__name__
    return wrapper