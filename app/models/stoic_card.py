from app import db


class StoicCard(db.Model):
    __tablename__ = 'stoic_card'

    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    author = db.Column(db.String(50), nullable=False)
    quote = db.Column(db.Text, nullable=False)
    principle = db.Column(db.String(100), nullable=False)
    bridge = db.Column(db.Text, nullable=False)

    entry = db.relationship('Entry', back_populates='stoic_cards')

    def __repr__(self):
        return f'<StoicCard {self.id}>'
