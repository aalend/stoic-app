from datetime import UTC, datetime

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=True)
    google_id = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))

    entries = db.relationship('Entry', back_populates='user')

    def __init__(self, name, email, password=None, google_id=None):
        self.name = name
        self.email = email
        self.password = password
        self.google_id = google_id

    def __repr__(self):
        return f'<User {self.email}>'
