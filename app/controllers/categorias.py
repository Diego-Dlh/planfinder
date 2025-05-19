from flask import Blueprint, render_template
from app.services.categorias import listar_categorias

bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@bp.route('/')
def index():
    categorias = listar_categorias()
    return render_template('categorias.html', categorias=categorias)
