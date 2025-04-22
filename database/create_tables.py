import sqlite3
from schema import SCHEMA, CSV_DIR


def create_connection():
    conn = sqlite3.connect('f1_info.db')
    cursor = conn.cursor()
    return conn, cursor


def create_tables(conn, cursor):
    for table, info in SCHEMA.items():
        s = f"CREATE TABLE {table} if not exists"
