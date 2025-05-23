from app import create_app, db
from app.models.usuario import Usuario
from app.models.plan import PlanTuristico
from app.models.resena import Resena
from app.models.favorito import Favorito
# importa todos los modelos

app = create_app()

with app.app_context():
    db.create_all()  # Esto crea las tablas si no existen

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
