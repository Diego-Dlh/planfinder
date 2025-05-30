from flask import Blueprint, render_template, request, redirect, url_for, session
from app.services.resenas import escribir_resena, obtener_resenas_por_plan

bp = Blueprint('resenas', __name__, url_prefix='/resenas')

@bp.route('/<int:plan_id>', methods=['POST'])
def reseñar(plan_id):
    if not session.get('usuario_id'):
        return redirect(url_for('auth.login'))
    else:
        calificacion = float(request.form['calificacion'])
        comentario = request.form['comentario']
        usuario_id = session.get('usuario_id')
        escribir_resena(usuario_id, plan_id, calificacion, comentario)
        return redirect(url_for('planes.detalle', plan_id=plan_id))  # ← redirige al detalle

