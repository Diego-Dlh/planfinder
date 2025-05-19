# app/controllers/main.py

from flask import Blueprint, render_template, request, session
from app.models.categoria import Categoria
from app.models.ubicacion import Ubicacion
from app.models.plan import PlanTuristico

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    usuario_id = session.get('usuario_id')

    # Captura de filtros desde la URL
    categoria_id = request.args.get('categoria_id')
    ubicacion_id = request.args.get('ubicacion_id')
    precio_min = request.args.get('precio_min')
    precio_max = request.args.get('precio_max')
    imagenes = request.args.get('imagenes')

    # Query base
    query = PlanTuristico.query

    if categoria_id:
        query = query.filter_by(categoria_id=categoria_id)
    if ubicacion_id:
        query = query.filter_by(ubicacion_id=ubicacion_id)
    if precio_min:
        query = query.filter(PlanTuristico.precio >= float(precio_min))
    if precio_max:
        query = query.filter(PlanTuristico.precio <= float(precio_max))
    if imagenes:
        query = query.filter(PlanTuristico.imagenes.any())

    planes = query.all()

    categorias = Categoria.query.all()
    ubicaciones = Ubicacion.query.all()

    return render_template(
        'home.html',
        planes=planes,
        usuario_id=usuario_id,
        categorias=categorias,
        ubicaciones=ubicaciones
    )
