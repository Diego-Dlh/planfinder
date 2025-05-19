from app import db

class Ubicacion(db.Model):
    __tablename__ = 'ubicaciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    coordenadas = db.Column(db.String(100))  # Ejemplo: "11.2435,-74.2023"
    tipo = db.Column(db.String(50))  # Playa, Museo, etc.

    planes = db.relationship('PlanTuristico', backref='ubicacion', lazy=True)
