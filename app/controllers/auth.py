from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from app.models.usuario import Usuario
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.contrasena, contrasena):
            login_user(usuario)  # Inicia la sesión del usuario
            session['usuario_id'] = usuario.id  # Guarda el ID del usuario en la sesión
            session['rol'] = usuario.tipo.value  # Guarda el rol en la sesión (Admin, Residente, etc.)
            flash('Bienvenido de nuevo!', 'success')
            return redirect(url_for('main.home'))  # Redirige a la página principal
        flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()  # Cierra la sesión del usuario
    flash('Has cerrado sesión correctamente.', 'success')
    return redirect(url_for('auth.login'))

# Función de autenticación (utilizada también en el servicio)
def autenticar_usuario(email, contrasena):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and check_password_hash(usuario.contrasena, contrasena):  # Compara el hash
        return {'ok': True, 'usuario': usuario}
    return {'ok': False, 'error': 'Credenciales inválidas'}
