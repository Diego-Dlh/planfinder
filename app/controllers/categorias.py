from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.categorias import listar_categorias, crear_categoria, editar_categoria, eliminar_categoria
from app.utils import admin_required  # Importamos el decorador

bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@bp.route('/index', methods=['GET'])
@admin_required  # Solo administradores pueden acceder a esta vista
def index():
    categorias = listar_categorias()
    return render_template('categorias.html', categorias=categorias)

@bp.route('/crear', methods=['GET', 'POST'])
@admin_required  # Solo administradores pueden crear categorías
def crear():
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']
        crear_categoria(nombre_categoria)
        flash("Categoría creada con éxito", "success")
        return redirect(url_for('categorias.index'))
    return render_template('crear_categoria.html')

from app.models.categoria import Categoria  # Asegúrate de importar el modelo correcto

@bp.route('/editar/<int:categoria_id>', methods=['GET', 'POST'])
@admin_required  # Solo administradores pueden editar categorías
def editar(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    
    if not categoria:
        flash("Categoría no encontrada", "danger")
        return redirect(url_for('categorias.index'))

    if request.method == 'POST':
        nuevo_nombre = request.form['nombre_categoria']
        editar_categoria(categoria_id, nuevo_nombre)
        flash("Categoría editada con éxito", "success")
        return redirect(url_for('categorias.index'))

    return render_template('editar_categoria.html', categoria=categoria)


@bp.route('/eliminar/<int:categoria_id>', methods=['POST'])
@admin_required  # Solo administradores pueden eliminar categorías
def eliminar(categoria_id):
    eliminar_categoria(categoria_id)
    flash("Categoría eliminada con éxito", "success")
    return redirect(url_for('categorias.index'))