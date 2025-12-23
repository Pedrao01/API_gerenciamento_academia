# from app import db
#
#
# class Payments(db.Model):
#     __tablename__ = 'registro_de_pagamento'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Text, unique=True, nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     amount_paid = db.Column(db.Float, nullable=False)
#     coach = db.Column(db.Text, nullable=False)
#
#     def __repr__(self):
#         return f'<user={self.username}>'
