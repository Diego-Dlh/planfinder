from app import db
from app.models.resena import Resena
from app.models.plan import PlanTuristico
from sqlalchemy import func
from app.models.usuario import Usuario


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
    resenas = (
        db.session.query(
            Resena.comentario,
            Resena.calificacion,
            Usuario.nombre.label('usuario_nombre')
        )
        .join(Usuario, Resena.usuario_id == Usuario.id)
        .filter(Resena.plan_id == plan_id)
        .order_by(Resena.id.desc())
        .all()
    )

    return [
        {
            'comentario': r.comentario,
            'calificacion': r.calificacion,
            'usuario_nombre': r.usuario_nombre
        }
        for r in resenas
    ]


from app.models.resena import Resena
import random

def obtener_resenas_aleatorias(n=3):
    todas = Resena.query.all()
    return random.sample(todas, min(n, len(todas)))
