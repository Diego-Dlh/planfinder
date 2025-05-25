from flask import Blueprint, redirect, request, url_for, flash, render_template
from app.services.admin import eliminar_resena,agregar_ubicacion, eliminar_ubicacion, listar_ubicaciones
from app.utils import admin_required  # Importar el decorador admin_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/eliminar-resena/<int:resena_id>')
@admin_required  # Usar el decorador para proteger esta ruta solo para administradores
def eliminar_resena_route(resena_id):
    resultado = eliminar_resena(resena_id)
    if resultado['ok']:
        flash('Reseña eliminada con éxito', 'success')
    else:
        flash(resultado['error'], 'danger')
    return redirect(url_for('planes.dashboard_admin'))  # Cambia a la ruta que desees redirigir

@bp.route('/agregar-ubicacion', methods=['GET', 'POST'])
@admin_required  # Usar el decorador para proteger esta ruta solo para administradores
def agregar_ubicacion_route():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        coordenadas = request.form['coordenadas']
        tipo = request.form['tipo']
        ubicacion = agregar_ubicacion(nombre, direccion, coordenadas, tipo)
        flash(f'Ubicación "{ubicacion.nombre}" agregada con éxito', 'success')
        return redirect(url_for('planes.dashboard_admin'))  # Cambia a la ruta que desees redirigir
    return render_template('agregar_ubicacion.html')

@bp.route('/eliminar-ubicacion/<int:ubicacion_id>')
@admin_required  # Usar el decorador para proteger esta ruta solo para administradores
def eliminar_ubicacion_route(ubicacion_id):
    resultado = eliminar_ubicacion(ubicacion_id)
    if resultado['ok']:
        flash('Ubicación eliminada con éxito', 'success')
    else:
        flash(resultado['error'], 'danger')
    return redirect(url_for('planes.dashboard_admin'))  # Cambia a la ruta que desees redirigir

@bp.route('/listar_ubicaciones')
@admin_required  # Usar el decorador para proteger esta ruta solo para administradores
def listar_ubicaciones_route():
    ubicaciones = listar_ubicaciones()
    return render_template('listar_ubicaciones.html', ubicaciones=ubicaciones)
