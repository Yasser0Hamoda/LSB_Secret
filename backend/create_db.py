''''
    This File Must Be Run For Only One Time To Create The Database
    From The Schema
'''
from config import DB_FILE_PATH, SCHEMA_FILE_PATH
import sqlite3

conn = sqlite3.connect(DB_FILE_PATH)
with open(SCHEMA_FILE_PATH) as f:
    schema = f.read()
    
cur = conn.executescript(schema)
conn.commit()
conn.close()
