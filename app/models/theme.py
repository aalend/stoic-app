from app import db
from app.models import entry_themes


class Theme(db.Model):
    __tablename__ = 'theme'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    entries = db.relationship('Entry', secondary=entry_themes, back_populates='themes')

    def __repr__(self):
        return f'<Theme {self.id}>'
