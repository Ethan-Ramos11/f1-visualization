import pandas as pd
from create_tables import create_connection
from schema import CSV_DIR, SCHEMA
import sqlite3
import os


def get_table_name(filename):
    for schema, info in SCHEMA:
        if info["file"] == filename:
            return schema


def read_csv():
    for filename in os.listdir(CSV_DIR):
        file_path = os.path.join(CSV_DIR, filename)
        file = pd.read_csv(file_path)
        for i in range(1, len(file)):
            table_name = SCHEMA[]


def insert_information(info, conn, cursor, table_name):
    s = f"""INSERT INTO TABLE {table_name}"""


def main():
    conn, cursor = create_connection()
