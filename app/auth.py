from flask import Blueprint, request, redirect, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?,?)",
            (request.form['username'], generate_password_hash(request.form['password']))
        )
        db.commit()
        return redirect('/login')
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=?",
            (request.form['username'],)
        ).fetchone()

        if user and check_password_hash(user['password_hash'], request.form['password']):
            session['user_id'] = user['id']
            return redirect('/')
    return render_template('login.html')
