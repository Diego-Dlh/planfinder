from app import create_app, db

# Importa tus modelos para que SQLAlchemy los reconozca
from app.models.usuario import Usuario
from app.models.plan import PlanTuristico
from app.models.resena import Resena
from app.models.favorito import Favorito
from app.models.administrador import Administrador
# importa todos los que tengas

app = create_app()

with app.app_context():
    db.create_all()
    print("Tablas creadas correctamente")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
