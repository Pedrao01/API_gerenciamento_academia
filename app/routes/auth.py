from flask import request, render_template, redirect, url_for, flash, Blueprint
# from app.models.payments import Payments
from app import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/')
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        coach = request.form.get('coach')
        gym_plan = request.form.get('plano')

        if not username or not email or not password or not coach or not gym_plan:
            flash('Error: all fields are mandatory!', 'error')
            return redirect(url_for('auth.register'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Error: Usuario já existe com o email informado', 'error')
            return redirect(url_for('auth.register'))

        new_user = User(username=username, email=email, coach=coach, gym_plan=gym_plan)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Error: All fields are mandatory!', 'error')
            return redirect(url_for('auth.login'))

        user = User.query.filter((User.email == email)).first()
        if user.check_password(password):
            flash('logged with successfully!', 'success')
            return redirect(url_for('main.dashboard'))
    return render_template('login.html')


@auth_bp.route('/register_payment', methods=['GET', 'POST'])
def register_payment():
    if request.method == 'POST':
        username = request.form.get('username')
        date = request.form.get('date')
        amount_paid = request.form.get('amount_paid')
        coach = request.form.get('coach')

        if not username or not date or not amount_paid or not coach:
            flash('All fields are mandatory', 'error')
            return redirect(url_for('auth.register_payment'))

        if Payments.query.filter((Payments.username == username)):
            return render_template('error.html')

        new_user = Payments(username=username, date=date, amount_paid=amount_paid, coach=coach)
        db.session.add(new_user)
        db.session.commit()

        flash('Gym member added with successfully!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register_payment.html')

