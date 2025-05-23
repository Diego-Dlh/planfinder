from app import create_app, db
from app.models.usuario import Usuario
from app.models.plan import PlanTuristico
from app.models.resena import Resena
from app.models.favorito import Favorito
# importa todos tus modelos aquí

app = create_app()

with app.app_context():
    db.create_all()
    print("Tablas creadas correctamente")
