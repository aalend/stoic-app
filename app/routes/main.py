from flask import Blueprint, redirect, render_template, session, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

    return render_template('journal/index.html')
