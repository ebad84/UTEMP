from flask import Blueprint, request, jsonify
from .db import get_db

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/upload', methods=['POST'])
def upload():
    db = get_db()
    key = request.headers.get('X-API-KEY')
    temp = request.json.get('temperature')

    sensor = db.execute("SELECT id FROM sensors WHERE api_key=?", (key,)).fetchone()
    if not sensor:
        return {'error': 'invalid key'}, 403

    db.execute("INSERT INTO sensor_data (sensor_id, temperature) VALUES (?,?)", (sensor['id'], temp))
    db.commit()
    return {'status': 'ok'}

@api_bp.route('/api/sensors')
def sensors():
    db = get_db()
    rows = db.execute(
        """
        SELECT
            s.name,
            s.uuid,
            sd.temperature,
            u.username
        FROM sensors s
        JOIN users u ON u.id = s.user_id
        LEFT JOIN sensor_data sd ON sd.id = (
            SELECT id FROM sensor_data
            WHERE sensor_id = s.id
            ORDER BY created_at DESC
            LIMIT 1
        )
        """
    ).fetchall()

    return jsonify([dict(r) for r in rows])
