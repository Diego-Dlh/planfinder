from app import db

class ImagenPlan(db.Model):
    __tablename__ = 'imagenes_plan'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('planes_turisticos.id'), nullable=False)
