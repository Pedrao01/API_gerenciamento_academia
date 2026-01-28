from functools import wraps
from flask import session, redirect, url_for, g, abort


def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorator


def role_required(*role):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            user = g.user

            if user is None:
                abort(401)
            if not user.has_any_role(*role):
                abort(403)

            return func(*args, **kwargs)
        return wrapped
    return decorator
