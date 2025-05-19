from app import db

class PlanTuristico(db.Model):
    __tablename__ = 'planes_turisticos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    duracion = db.Column(db.Float)
    promedio_calificacion = db.Column(db.Float)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicaciones.id'))

    imagenes = db.relationship('ImagenPlan', backref='plan', lazy=True)
    resenas = db.relationship('Resena', backref='plan', lazy=True)
    transportes = db.relationship('AlternativaDeTransporte', backref='plan', lazy=True)
