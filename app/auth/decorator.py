from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorator