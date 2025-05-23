from app import db
from datetime import date

from app.models.plan import PlanTuristico  # si no está ya importado

class Favorito(db.Model):
    __tablename__ = 'favoritos'

    id = db.Column(db.Integer, primary_key=True)
    fecha_guardado = db.Column(db.Date, default=date.today)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('planes_turisticos.id'), nullable=False)

    plan = db.relationship('PlanTuristico', backref='favoritos', lazy=True)
