from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()

# Crear instancia de LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Define qué ruta se usará para el login

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa db y LoginManager
    db.init_app(app)
    login_manager.init_app(app)

    # Registrar Blueprints (asegurate de tenerlos configurados)
    from app.controllers import usuarios, planes, resenas, favoritos, auth, admin, main, categorias
    app.register_blueprint(categorias.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(planes.bp)
    app.register_blueprint(resenas.bp)
    app.register_blueprint(favoritos.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)
    
    return app
# Cargar el usuario desde la base de datos
from flask_login import LoginManager
from app.models.usuario import Usuario

# Usuario Loader
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
