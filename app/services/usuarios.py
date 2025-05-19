from app import db
from app.models.usuario import Usuario, TipoUsuario
from sqlalchemy.exc import IntegrityError

def registrar_usuario(nombre, email, contrasena, tipo=TipoUsuario.TURISTA, foto_perfil=None):
    nuevo = Usuario(
        nombre=nombre,
        email=email,
        contrasena=contrasena,
        tipo=tipo,
        foto_perfil=foto_perfil
    )
    db.session.add(nuevo)
    try:
        db.session.commit()
        return {'ok': True}
    except IntegrityError:
        db.session.rollback()
        return {'ok': False, 'error': 'El correo ya está registrado'}

def listar_usuarios():
    return Usuario.query.all()

def obtener_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)
