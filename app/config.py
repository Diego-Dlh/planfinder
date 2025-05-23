import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto_seguro')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Aquí no uses valor por defecto en prod
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Mejor dejar False para prod, mejora rendimiento
