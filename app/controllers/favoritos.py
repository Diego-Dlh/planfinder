from flask import Blueprint, redirect, url_for, session, render_template
from app.services.favoritos import guardar_favorito, listar_favoritos

bp = Blueprint('favoritos', __name__, url_prefix='/favoritos')

@bp.route('/agregar/<int:plan_id>')
def agregar(plan_id):
    usuario_id = session.get('usuario_id')
    guardar_favorito(usuario_id, plan_id)
    return redirect(url_for('favoritos.listar'))

@bp.route('/')
def listar():
    usuario_id = session.get('usuario_id')
    favoritos = listar_favoritos(usuario_id)
    return render_template('favoritos.html', favoritos=favoritos)
