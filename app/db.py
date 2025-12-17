import sqlite3
from flask import g

DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db:
        db.close()

def init_db(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        db = get_db()
        with open('app/models.sql') as f:
            db.executescript(f.read())
        db.commit()
