from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.usuarios import registrar_usuario, listar_usuarios

bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['email']
        contrasena = request.form['contrasena']
        resultado = registrar_usuario(nombre, correo, contrasena)
        if resultado['ok']:
            flash('Usuario registrado con éxito')
            return redirect(url_for('auth.login'))
        flash(resultado['error'])
    return render_template('registro.html')

@bp.route('/listar')
def listar():
    usuarios = listar_usuarios()
    return render_template('usuarios_listar.html', usuarios=usuarios)

from flask import session, render_template, request, redirect, url_for, flash
from app.models.usuario import Usuario
from app import db

from werkzeug.security import generate_password_hash

@bp.route('/perfil', methods=['GET', 'POST'])
def perfil():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash('Debes iniciar sesión.')
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(usuario_id)

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        nueva_contrasena = request.form['contrasena']
        foto = request.form['foto_perfil']

        if nueva_contrasena:
            usuario.contrasena = generate_password_hash(nueva_contrasena)
        if foto:
            usuario.foto_perfil = foto

        db.session.commit()
        flash('Perfil actualizado correctamente.')
        return redirect(url_for('usuarios.perfil'))

    return render_template('perfil.html', usuario=usuario)
