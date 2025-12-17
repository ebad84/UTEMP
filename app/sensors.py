from flask import Blueprint, render_template, request, redirect, session
from .db import get_db
import uuid, secrets

sensors_bp = Blueprint('sensors', __name__)

def gen_uuid(): return str(uuid.uuid4())
def gen_key(): return secrets.token_hex(32)

@sensors_bp.route('/')
def index():
    return render_template('index.html')

@sensors_bp.route('/new-sensor', methods=['GET', 'POST'])
def new_sensor():
    if request.method == 'POST':
        db = get_db()
        db.execute(
            "INSERT INTO sensors (user_id, name, description, uuid, api_key) VALUES (?,?,?,?,?)",
            (session.get('user_id'), request.form['name'], request.form['description'], gen_uuid(), gen_key())
        )
        db.commit()
        return redirect('/')
    return render_template('new_sensor.html')
