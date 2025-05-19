from app import db
from sqlalchemy import Enum
import enum

class RolAdministrador(enum.Enum):
    SUPERADM = "superAdm"
    MODERA = "Modera"
    GESTOR = "Gestor"

class Administrador(db.Model):
    __tablename__ = 'administradores'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.Enum(RolAdministrador), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), unique=True)
