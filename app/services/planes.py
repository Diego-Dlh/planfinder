from app import db
from app.models.plan import PlanTuristico

def crear_plan(nombre, descripcion, precio, duracion, usuario_id, categoria_id, ubicacion_id):
    plan = PlanTuristico(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        duracion=duracion,
        usuario_id=usuario_id,
        categoria_id=categoria_id,
        ubicacion_id=ubicacion_id
    )
    db.session.add(plan)
    db.session.commit()
    return plan

def listar_planes():
    return PlanTuristico.query.all()

def obtener_plan_por_id(plan_id):
    return PlanTuristico.query.get(plan_id)

def actualizar_plan(plan, nombre, descripcion, precio, duracion, categoria_id, ubicacion_id):
    plan.nombre = nombre
    plan.descripcion = descripcion
    plan.precio = precio
    plan.duracion = duracion
    plan.categoria_id = categoria_id
    plan.ubicacion_id = ubicacion_id
    db.session.commit()
    return plan

def eliminar_plan(plan):
    db.session.delete(plan)
    db.session.commit()
