from app import create_app, db
from app.models.usuario import Usuario
from app.models.plan import PlanTuristico
from app.models.resena import Resena
from app.models.favorito import Favorito
from app.models.administrador import Administrador
# importa aquí todos tus modelos

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente")
    app.run(host="0.0.0.0", port=5000, debug=False)
