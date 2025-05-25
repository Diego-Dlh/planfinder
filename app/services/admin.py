from app.models.resena import Resena
from app.models.ubicacion import Ubicacion
from app import db

def eliminar_resena(resena_id):
    resena = Resena.query.get(resena_id)
    if resena:
        db.session.delete(resena)
        db.session.commit()
        return {'ok': True}
    return {'ok': False, 'error': 'Reseña no encontrada'}

def agregar_ubicacion(nombre, direccion='', coordenadas='', tipo=''):
    nueva = Ubicacion(
        nombre=nombre,
        direccion=direccion,
        coordenadas=coordenadas,
        tipo=tipo
    )
    db.session.add(nueva)
    db.session.commit()
    return nueva

def eliminar_ubicacion(ubicacion_id):
    ubicacion = Ubicacion.query.get(ubicacion_id)
    if ubicacion:
        db.session.delete(ubicacion)
        db.session.commit()
        return {'ok': True}
    return {'ok': False, 'error': 'Ubicación no encontrada'}

def listar_ubicaciones():
    return Ubicacion.query.all()