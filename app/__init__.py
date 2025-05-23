from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importa blueprints y regístralos
    from app.controllers import usuarios, planes, resenas, favoritos, auth, admin, main
    app.register_blueprint(main.bp)
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(planes.bp)
    app.register_blueprint(resenas.bp)
    app.register_blueprint(favoritos.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    return app
