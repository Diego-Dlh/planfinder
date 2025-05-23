from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # CREA TODAS LAS TABLAS según los modelos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
