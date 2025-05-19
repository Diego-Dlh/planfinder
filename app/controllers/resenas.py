from flask import Blueprint, render_template, request, redirect, url_for, session
from app.services.resenas import escribir_resena, obtener_resenas_por_plan

bp = Blueprint('resenas', __name__, url_prefix='/resenas')

@bp.route('/<int:plan_id>', methods=['GET', 'POST'])
def reseñar(plan_id):
    if request.method == 'POST':
        calificacion = float(request.form['calificacion'])
        comentario = request.form['comentario']
        usuario_id = session.get('usuario_id')
        escribir_resena(usuario_id, plan_id, calificacion, comentario)
        return redirect(url_for('resenas.reseñar', plan_id=plan_id))
    resenas = obtener_resenas_por_plan(plan_id)
    return render_template('resenas.html', resenas=resenas, plan_id=plan_id)
