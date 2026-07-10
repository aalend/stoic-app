from datetime import UTC, datetime

from app import db
from app.models import entry_themes


class Entry(db.Model):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))

    user = db.relationship('User', back_populates='entries')
    stoic_cards = db.relationship('StoicCard', back_populates='entry')
    themes = db.relationship('Theme', secondary=entry_themes, back_populates='entries')

    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def __repr__(self):
        return f'<Entry {self.id}>'
