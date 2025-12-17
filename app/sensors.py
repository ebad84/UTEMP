from flask import Blueprint, render_template, request, redirect, session
from .db import get_db
import uuid, secrets

sensors_bp = Blueprint('sensors', __name__)

def gen_uuid(): return str(uuid.uuid4())
def gen_key(): return secrets.token_hex(32)

@sensors_bp.route('/')
def index():
    return render_template('index.html', logged_in=('user_id' in session))


@sensors_bp.route('/new-sensor', methods=['GET', 'POST'])
def new_sensor():
    if request.method == 'POST':
        sensor_uuid = gen_uuid()
        api_key = gen_key()

        db = get_db()
        db.execute(
            "INSERT INTO sensors (user_id, name, description, uuid, api_key) VALUES (?,?,?,?,?)",
            (
                session.get('user_id'),
                request.form['name'],
                request.form['description'],
                sensor_uuid,
                api_key
            )
        )
        db.commit()

        return render_template(
            'sensor_created.html',
            uuid=sensor_uuid,
            api_key=api_key
        )

    return render_template('new_sensor.html')
