from flask import Blueprint, redirect, url_for, session, render_template, flash
from app.services.favoritos import eliminar_favorito, guardar_favorito, listar_favoritos

bp = Blueprint('favoritos', __name__, url_prefix='/favoritos')


@bp.route('/agregar/<int:plan_id>')
def agregar(plan_id):
    usuario_id = session.get('usuario_id')
    resultado = guardar_favorito(usuario_id, plan_id)
    if resultado['ok']:
        flash('Plan agregado a favoritos')
    else:
        flash(resultado['error'])
    return redirect(url_for('favoritos.listar'))


@bp.route('/')
def listar():
    usuario_id = session.get('usuario_id')
    favoritos = listar_favoritos(usuario_id)
    return render_template('favoritos.html', favoritos=favoritos)


@bp.route('/eliminar/<int:plan_id>')
def eliminar(plan_id):
    usuario_id = session.get('usuario_id')
    resultado = eliminar_favorito(usuario_id, plan_id)
    if resultado['ok']:
        flash('Plan eliminado de favoritos')
    else:
        flash(resultado['error'])
    return redirect(url_for('favoritos.listar'))
