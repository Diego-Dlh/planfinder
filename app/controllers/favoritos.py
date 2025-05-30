from flask import Blueprint, redirect, url_for, session, render_template, flash
from app.services.favoritos import eliminar_favorito, guardar_favorito, listar_favoritos
from app.utils import admin_required  # Importamos el decorador para protección

bp = Blueprint('favoritos', __name__, url_prefix='/favoritos')

@bp.route('/agregar/<int:plan_id>')
def agregar(plan_id):
    if not session.get('usuario_id'):
        flash("Debes iniciar sesión para agregar favoritos", "danger")
        return redirect(url_for('auth.login'))
    else:
        usuario_id = session.get('usuario_id')
        resultado = guardar_favorito(usuario_id, plan_id)
        if resultado['ok']:
            flash('Plan agregado a favoritos', 'success')
        else:
            flash(resultado['error'], 'danger')
            return redirect(url_for('favoritos.listar'))

@bp.route('/')
def listar():
    usuario_id = session.get('usuario_id')

    if not usuario_id:
        flash("Debes iniciar sesión para ver tus favoritos", "danger")
        return redirect(url_for('auth.login'))  # Redirige a login si no está logueado

    favoritos = listar_favoritos(usuario_id)
    return render_template('favoritos.html', favoritos=favoritos)

@bp.route('/eliminar/<int:plan_id>')
def eliminar(plan_id):
    usuario_id = session.get('usuario_id')
    resultado = eliminar_favorito(usuario_id, plan_id)
    if resultado['ok']:
        flash('Plan eliminado de favoritos', 'success')
    else:
        flash(resultado['error'], 'danger')
    return redirect(url_for('favoritos.listar'))
