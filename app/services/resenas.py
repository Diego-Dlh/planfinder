from app import db
from app.models.resena import Resena

def escribir_resena(usuario_id, plan_id, calificacion, comentario):
    nueva = Resena(
        usuario_id=usuario_id,
        plan_id=plan_id,
        calificacion=calificacion,
        comentario=comentario
    )
    db.session.add(nueva)
    db.session.commit()
    return nueva

def obtener_resenas_por_plan(plan_id):
    return Resena.query.filter_by(plan_id=plan_id).all()
