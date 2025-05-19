from app import db
from app.models.favorito import Favorito

def guardar_favorito(usuario_id, plan_id):
    existente = Favorito.query.filter_by(usuario_id=usuario_id, plan_id=plan_id).first()
    if existente:
        return {'ok': False, 'error': 'Ya está guardado como favorito'}
    nuevo = Favorito(usuario_id=usuario_id, plan_id=plan_id)
    db.session.add(nuevo)
    db.session.commit()
    return {'ok': True}

def listar_favoritos(usuario_id):
    return Favorito.query.filter_by(usuario_id=usuario_id).all()
