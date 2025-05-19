from app.models.categoria import Categoria

def listar_categorias():
    return Categoria.query.all()
