import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '123456789')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123456@localhost:5432/planfinder')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
