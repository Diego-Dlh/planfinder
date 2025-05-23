from app.models.usuario import Usuario
from werkzeug.security import check_password_hash

def autenticar_usuario(email, contrasena):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and check_password_hash(usuario.contrasena, contrasena):
        return {'ok': True, 'usuario': usuario}
    return {'ok': False, 'error': 'Credenciales inválidas'}
