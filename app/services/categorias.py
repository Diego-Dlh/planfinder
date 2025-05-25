from app.models.categoria import Categoria
from app import db


def listar_categorias():
    return Categoria.query.all()

def crear_categoria(nombre):
    # Crear una nueva categoría y guardarla en la base de datos
    nueva_categoria = Categoria(nombre=nombre)
    db.session.add(nueva_categoria)
    db.session.commit()

def editar_categoria(categoria_id, nuevo_nombre):
    # Editar el nombre de una categoría existente
    categoria = Categoria.query.get(categoria_id)
    if categoria:
        categoria.nombre = nuevo_nombre
        db.session.commit()
    return categoria

def eliminar_categoria(categoria_id):
    # Eliminar una categoría existente
    categoria = Categoria.query.get(categoria_id)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
    return categoria