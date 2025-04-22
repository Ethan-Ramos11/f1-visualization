import sqlite3


def create_connection():
    conn = sqlite3.connect('f1_info.db')
    cursor = conn.cursor()
    return conn, cursor



