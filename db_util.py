from flask import _app_ctx_stack
import sqlite3
import server

def get_db():
    sqlite_db = sqlite3.connect(server.app.config['DATABASE'])
    sqlite_db.row_factory = sqlite3.Row
    return sqlite_db;

def init_db():
    """Creates the database tables."""
    db = get_db()
    c = db.cursor();
    with open('schema.sql')  as f:
        c.executescript(f.read())
    db.commit()
