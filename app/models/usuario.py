from flask_login import UserMixin
from app import db
import enum

class TipoUsuario(enum.Enum):
    TURISTA = "Turista"
    RESIDENTE = "Residente"
    ADMIN = "Admin"

class Usuario(db.Model, UserMixin):  # Hereda de UserMixin
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.Enum(TipoUsuario), nullable=False)
    foto_perfil = db.Column(db.String(255))

    planes = db.relationship('PlanTuristico', backref='creador', lazy=True)
    resenas = db.relationship('Resena', backref='autor', lazy=True)
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)

    # Añadir el método get_id que es necesario para Flask-Login
    def get_id(self):
        return str(self.id)  # Debe retornar el ID como string

