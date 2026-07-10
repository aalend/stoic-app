from flask import Blueprint, redirect, render_template, request, session, url_for

from app import db
from app.models.entry import Entry
from app.models.stoic_card import StoicCard
from app.models.theme import Theme
from app.services.ai import get_stoic_wisdom

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

    result = None

    if request.method == 'POST':
        entry_text = request.form.get('entry_text')
        result = get_stoic_wisdom(entry_text)

        if result:
            new_entry = Entry(user_id=session.get('user_id'), text=entry_text)
            db.session.add(new_entry)
            db.session.flush()

            for theme_name in result['themes']:
                existing_theme = Theme.query.filter_by(name=theme_name).first()

                if not existing_theme:
                    existing_theme = Theme(name=theme_name)
                    db.session.add(existing_theme)
                    db.session.flush()
                new_entry.themes.append(existing_theme)

            for card in result['cards']:
                new_card = StoicCard(
                    entry_id=new_entry.id,
                    author=card['author'],
                    quote=card['quote'],
                    principle=card['principle'],
                    bridge=card['bridge'],
                )
                db.session.add(new_card)

            db.session.commit()

    return render_template('journal/index.html', result=result)


@main.route('/history')
def history():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

    entries = Entry.query.filter_by(user_id=session.get('user_id')).all()

    return render_template('journal/history.html', entries=entries)
