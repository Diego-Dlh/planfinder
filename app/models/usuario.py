from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
import enum

class TipoUsuario(enum.Enum):
    TURISTA = "Turista"
    RESIDENTE = "Residente"
    ADMIN = "Admin"

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.Enum(TipoUsuario), nullable=False)
    foto_perfil = db.Column(db.String(255))

    planes = relationship('PlanTuristico', backref='creador', lazy=True)
    resenas = relationship('Resena', backref='autor', lazy=True)
    favoritos = relationship('Favorito', backref='usuario', lazy=True)
    sesion = relationship('Sesion', uselist=False, backref='usuario')
