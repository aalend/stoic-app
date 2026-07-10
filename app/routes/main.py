from flask import Blueprint, flash, redirect, render_template, request, session, url_for

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

        if result is None:
            flash('AI service is not allowed.', 'error')

    return render_template('journal/index.html', result=result)
