# ruff: noqa: E402

from app import db

entry_themes = db.Table(
    'entry_themes',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'), primary_key=True),
    db.Column('theme_id', db.Integer, db.ForeignKey('theme.id'), primary_key=True),
)


from app.models.entry import Entry
from app.models.stoic_card import StoicCard
from app.models.theme import Theme
from app.models.user import User
