from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt

from app import db
from app.models import User

bcrypt = Bcrypt()

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email already exist
        existing_user = User.query.filter_by(email=email).first()
        print(existing_user)
        if existing_user:
            flash('Email already exist.', 'error')
            return redirect(url_for('auth.register'))

        # Generate hashed password
        hashed_password = bcrypt.generate_password_hash(password).decode('utc-8')

        # Save user
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Save to session and redirect
        session['user_id'] = new_user.id
        return redirect(url_for('main.index'))

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email already exist
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            flash('Email not exist', 'error')
            return redirect(url_for('auth.login'))

        # Check hashed password
        hashed_password = bcrypt.check_password_hash(existing_user.password, password)
        if hashed_password:
            # Save user to session
            session['user_id'] = existing_user.id
            return redirect(url_for('main.index'))

    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('auth.login'))
