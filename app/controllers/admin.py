from flask import Blueprint, redirect, url_for, flash
from app.services.admin import eliminar_resena
from app.utils import admin_required  # Importar el decorador admin_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/eliminar-resena/<int:resena_id>')
@admin_required  # Usar el decorador para proteger esta ruta solo para administradores
def eliminar_resena_route(resena_id):
    resultado = eliminar_resena(resena_id)
    if resultado['ok']:
        flash('Reseña eliminada con éxito', 'success')
    else:
        flash(resultado['error'], 'danger')
    return redirect(url_for('planes.listar'))

