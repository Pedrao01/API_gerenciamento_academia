# from flask import request, render_template, redirect, url_for, flash, Blueprint
# from sqlalchemy import func, text
# from app.models.payments import Payments
#
#
# debtor_bp = Blueprint('debtor', __name__, template_folder='templates')
#
#
# @debtor_bp.route('/debtor', methods=['GET', 'POST'])
# def all_debtors():
#     query = Payments.query.filter(
#         func.now() >= Payments.date + text("INTERVAL '1 month'")
#     ).all()
#     return render_template('debtor.html', informacoes=query)
