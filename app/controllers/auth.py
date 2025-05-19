from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth import autenticar_usuario

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        resultado = autenticar_usuario(email, contrasena)
        if resultado['ok']:
            session['usuario_id'] = resultado['usuario'].id
            flash('Sesión iniciada correctamente')
            return redirect(url_for('planes.listar'))
        flash(resultado['error'])
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada')
    return redirect(url_for('auth.login'))
