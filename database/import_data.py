import pandas as pd
from create_tables import create_connection
from schema import CSV_DIR, SCHEMA
import sqlite3
import os


def get_table_name(filename):
    for schema, info in SCHEMA:
        if info["file"] == filename:
            return schema


def read_csv(conn, cursor):
    for filename in os.listdir(CSV_DIR):
        if not filename.endswith(".csv"):
            continue
        file_path = os.path.join(CSV_DIR, filename)
        table_name = get_table_name(filename)
        if not table_name:
            continue
        file = pd.read_csv(file_path)
        for i in range(1, len(file)):
            insert_information(file[i], conn, cursor, table_name)


def insert_information(info, conn, cursor, table_name):
    s = f"""INSERT INTO TABLE {table_name} 
        ()
        """


def main():
    conn, cursor = create_connection()
