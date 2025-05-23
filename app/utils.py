from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica si el rol en la sesión es 'Admin'
        if session.get('rol') != 'Admin':
            flash("Acceso denegado. Solo administradores pueden acceder.", 'danger')
            return redirect(url_for('auth.login'))  # Redirige al login si no es admin
        return f(*args, **kwargs)
    return decorated_function
