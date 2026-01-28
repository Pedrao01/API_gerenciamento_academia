from flask import Blueprint, request, render_template, redirect, url_for, flash, session, g
from app.auth.decorator import login_required

main_bp = Blueprint('main', __name__, template_folder='templates')


@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        pass

    return render_template('dashboard.html')


@main_bp.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect(url_for('auth.login'))