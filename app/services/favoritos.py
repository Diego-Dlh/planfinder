from app import db
from app.models.favorito import Favorito


def guardar_favorito(usuario_id, plan_id):
    existente = Favorito.query.filter_by(usuario_id=usuario_id, plan_id=plan_id).first()
    if existente:
        return {'ok': False, 'error': 'El plan ya está guardado en tus favoritos'}
    
    nuevo = Favorito(usuario_id=usuario_id, plan_id=plan_id)
    db.session.add(nuevo)
    db.session.commit()
    return {'ok': True}


def listar_favoritos(usuario_id):
    return Favorito.query.filter_by(usuario_id=usuario_id).all()


def eliminar_favorito(usuario_id, plan_id):
    favorito = Favorito.query.filter_by(usuario_id=usuario_id, plan_id=plan_id).first()
    if favorito:
        db.session.delete(favorito)
        db.session.commit()
        return {'ok': True}
    return {'ok': False, 'error': 'El plan no estaba en favoritos'}
