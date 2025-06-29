from model import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_names = db.Column(db.String(100), nullable=False)
    first_lastname = db.Column(db.String(100), nullable=False)
    second_lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def verificar_contraseña(self, password_plano):
        return check_password_hash(self.password, password_plano)
