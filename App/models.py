
from datetime import datetime
from App import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)