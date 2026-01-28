from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from .role import user_roles
from flask import session, g


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    coach = db.Column(db.String(80), nullable=True)
    gym_plan = db.Column(db.String(80), nullable=True)

    roles = db.Relationship('Role', secondary=user_roles, backref='users')

    def __repr__(self):
        return f'<user={self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

    def has_any_role(self, *role_name):
        return any(role.name in role_name for role in self.roles)