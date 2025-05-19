from flask import Blueprint, redirect, url_for, flash
from app.services.admin import eliminar_resena

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/eliminar-resena/<int:resena_id>')
def eliminar_resena_route(resena_id):
    resultado = eliminar_resena(resena_id)
    if resultado['ok']:
        flash('Reseña eliminada con éxito')
    else:
        flash(resultado['error'])
    return redirect(url_for('planes.listar'))
