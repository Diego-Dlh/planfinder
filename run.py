from app import create_app, db

# Importa todos tus modelos para que SQLAlchemy los conozca
from app.models.usuario import Usuario
from app.models.plan import PlanTuristico
from app.models.resena import Resena
from app.models.favorito import Favorito
from app.models.administrador import Administrador
# agrega aquí todos los modelos que uses

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            print("Tablas creadas correctamente")
        except Exception as e:
            print("Error creando tablas:", e)
    app.run(host="0.0.0.0", port=5000, debug=False)
