import sqlite3
from schema import SCHEMA, CSV_DIR


def create_connection():
    conn = sqlite3.connect('f1_info.db')
    cursor = conn.cursor()
    return conn, cursor





def convert_to_sql_columns(info):
    s = ""
    for key, val in info.items():
        s += f"{key} {val},"
    return s[:-1]
