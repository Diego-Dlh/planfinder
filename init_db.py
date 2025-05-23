from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configparser import Config

db = SQLAlchemy()
migrate = Migrate()  # Instancia global

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # Inicializa migraciones con app y db

    # Registro blueprints...
    from app.controllers import usuarios, planes, resenas, favoritos, auth, admin, main
    app.register_blueprint(main.bp)
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(planes.bp)
    app.register_blueprint(resenas.bp)
    app.register_blueprint(favoritos.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    return app
