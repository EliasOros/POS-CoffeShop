from flask import Blueprint, render_template, request, redirect, flash
from model.user import User
from model import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('username')
        contraseña = request.form.get('password')

        usuario = User.query.filter_by(email=correo).first()

        if usuario and usuario.verificar_contraseña(contraseña):

            return f"Bienvenida, {usuario.first_names} "
            
        else:
            flash("Correo o contraseña incorrectos.", "error")
            return redirect('/login')

    return render_template('cardProduct.html')
