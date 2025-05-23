from app import db
from app.models.resena import Resena
from app.models.plan import PlanTuristico
from sqlalchemy import func

def escribir_resena(usuario_id, plan_id, calificacion, comentario):
    nueva = Resena(
        usuario_id=usuario_id,
        plan_id=plan_id,
        calificacion=calificacion,
        comentario=comentario
    )
    db.session.add(nueva)
    db.session.commit()

    # Actualiza el promedio de calificaciones del plan
    nuevo_promedio = db.session.query(func.avg(Resena.calificacion)).filter_by(plan_id=plan_id).scalar()
    plan = PlanTuristico.query.get(plan_id)
    plan.promedio_calificacion = round(nuevo_promedio, 2)
    db.session.commit()

    return nueva

def obtener_resenas_por_plan(plan_id):
    return Resena.query.filter_by(plan_id=plan_id).all()
