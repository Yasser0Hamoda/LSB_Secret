import sqlite3
from config import DB_FILE_PATH

def get_db_conn():
    conn = sqlite3.connect(DB_FILE_PATH)
    # conn.row_factory = sqlite3.Row
    return conn