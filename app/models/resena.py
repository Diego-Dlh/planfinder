from app import db
from datetime import date

class Resena(db.Model):
    __tablename__ = 'resenas'

    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Float, nullable=False)
    comentario = db.Column(db.Text)
    fecha = db.Column(db.Date, default=date.today)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('planes_turisticos.id'), nullable=False)
