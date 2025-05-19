from app import db

class AlternativaDeTransporte(db.Model):
    __tablename__ = 'alternativas_transporte'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.Time)
    descripcion = db.Column(db.Text)

    plan_id = db.Column(db.Integer, db.ForeignKey('planes_turisticos.id'), nullable=False)
