from app4 import db
from datetime import datetime
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime,nullable=False)

    def __repr__(self):
        return f"Title('{self.title}')' Created on Date('{self.date})"