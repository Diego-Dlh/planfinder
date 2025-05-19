from app import db

class Sesion(db.Model):
    __tablename__ = 'sesiones'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    fecha_inicio = db.Column(db.DateTime)
    fecha_expiracion = db.Column(db.DateTime)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False, unique=True)
