from app.models.resena import Resena
from app import db

def eliminar_resena(resena_id):
    resena = Resena.query.get(resena_id)
    if resena:
        db.session.delete(resena)
        db.session.commit()
        return {'ok': True}
    return {'ok': False, 'error': 'Reseña no encontrada'}
