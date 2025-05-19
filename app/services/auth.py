from app.models.usuario import Usuario

def autenticar_usuario(email, contrasena):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and usuario.contrasena == contrasena:
        return {'ok': True, 'usuario': usuario}
    return {'ok': False, 'error': 'Credenciales inválidas'}
