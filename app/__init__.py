from flask import Flask
from .db import init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'dev-secret-key'

    init_db(app)

    from .auth import auth_bp
    from .sensors import sensors_bp
    from .api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(sensors_bp)
    app.register_blueprint(api_bp)

    return app
