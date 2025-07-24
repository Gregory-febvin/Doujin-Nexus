# app/database.py
import os
import sqlite3
from contextlib import closing

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '../Database/nhentai_metadata.db')


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=()):
    try:
        with closing(get_db_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def fetch_one(query, params=()):
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

def fetch_all(query, params=()):
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
