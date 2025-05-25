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
    usuario_id = session.get('usuario_id')

    # Captura de filtros desde la URL
    categoria_id = request.args.get('categoria_id')
    ubicacion_id = request.args.get('ubicacion_id')
    precio_min = request.args.get('precio_min')
    precio_max = request.args.get('precio_max')
    imagenes = request.args.get('imagenes')

    # Query base
    from app.models.plan import PlanTuristico
    from app.models.categoria import Categoria
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
        'planes_listar.html',
        planes=planes,
        categorias=categorias,
        ubicaciones=ubicaciones,
        usuario_id=usuario_id
    )


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

# Editar un plan
@bp.route('/<int:plan_id>/editar', methods=['GET', 'POST'])
@admin_required
def editar(plan_id):
    from app.models.categoria import Categoria
    plan = obtener_plan_por_id(plan_id)
    categorias = Categoria.query.all()
    ubicaciones = Ubicacion.query.all()
    
    if request.method == 'POST':
        plan.nombre = request.form['nombre']
        plan.descripcion = request.form['descripcion']
        plan.precio = float(request.form['precio'])
        plan.duracion = float(request.form['duracion'])
        plan.categoria_id = request.form['categoria_id']
        plan.ubicacion_id = request.form['ubicacion_id']
        db.session.commit()
        flash('Plan actualizado exitosamente', 'success')
        return redirect(url_for('planes.dashboard_admin'))
    
    return render_template('editar_plan.html', plan=plan, categorias=categorias, ubicaciones=ubicaciones)

# Eliminar un plan
@bp.route('/<int:plan_id>/eliminar', methods=['POST'])
@admin_required
def eliminar(plan_id):
    plan = obtener_plan_por_id(plan_id)
    db.session.delete(plan)
    db.session.commit()
    flash('Plan eliminado correctamente', 'success')
    return redirect(url_for('planes.dashboard_admin'))

# Vista general del dashboard de planes (solo admins)
@bp.route('/admin/dashboard')
@admin_required
def dashboard_admin():
    from app.models.plan import PlanTuristico
    planes = PlanTuristico.query.order_by(PlanTuristico.nombre).all()
    return render_template('dashboard_planes.html', planes=planes)