from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.categorias import listar_categorias, crear_categoria
from app.utils import admin_required  # Importamos el decorador

bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@bp.route('/')
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
