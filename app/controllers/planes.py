from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.planes import listar_planes, crear_plan, obtener_plan_por_id
from app.models.imagen_plan import ImagenPlan
from app.models.ubicacion import Ubicacion
from app import db
from app.utils import admin_required  # Importamos el decorador

bp = Blueprint('planes', __name__, url_prefix='/planes')

# Listado de planes
@bp.route('/')
def listar():
    planes = listar_planes()
    return render_template('planes_listar.html', planes=planes)

# Crear nuevo plan (solo administrador)
@bp.route('/nuevo', methods=['GET', 'POST'])
@admin_required  # Solo administradores pueden crear planes
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        duracion = float(request.form['duracion'])
        categoria_id = request.form['categoria_id']
        ubicacion_id = request.form['ubicacion_id']
        usuario_id = session.get('usuario_id')
        plan = crear_plan(nombre, descripcion, precio, duracion, usuario_id, categoria_id, ubicacion_id)
        flash('Plan creado exitosamente', 'success')
        return redirect(url_for('planes.listar'))
    return render_template('crear_plan.html')

# Detalle de plan turístico (todos los usuarios pueden verlo)
@bp.route('/<int:plan_id>')
def detalle(plan_id):
    from app.services.resenas import obtener_resenas_por_plan  # Importación dentro de la función para evitar bucles
    plan = obtener_plan_por_id(plan_id)
    resenas = obtener_resenas_por_plan(plan_id)
    imagenes = plan.imagenes
    ubicacion = plan.ubicacion
    usuario_id = session.get('usuario_id')
    return render_template(
        'detalle_plan.html',
        plan=plan,
        resenas=resenas,
        imagenes=imagenes,
        ubicacion=ubicacion,
        usuario_id=usuario_id
    )

# Agregar imagen a un plan (solo administrador)
@bp.route('/<int:plan_id>/agregar-imagen', methods=['GET', 'POST'])
@admin_required  # Solo administradores pueden agregar imágenes
def agregar_imagen(plan_id):
    if request.method == 'POST':
        url = request.form['url']
        imagen = ImagenPlan(url=url, plan_id=plan_id)
        db.session.add(imagen)
        db.session.commit()
        flash('Imagen agregada correctamente.', 'success')
        return redirect(url_for('planes.detalle', plan_id=plan_id))
    return render_template('agregar_imagen.html', plan_id=plan_id)