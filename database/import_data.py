import pandas as pd
from create_tables import create_connection
from schema import CSV_DIR, SCHEMA
import sqlite3
import os


def get_table_name(filename):
    for schema, info in SCHEMA.items():
        if info["file"] == filename:
            return schema


def get_columns(table_name, cursor):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]
    return columns


def read_csv(conn, cursor):
    for filename in os.listdir(CSV_DIR):
        if not filename.endswith(".csv"):
            continue
        file_path = os.path.join(CSV_DIR, filename)
        table_name = get_table_name(filename)
        if not table_name:
            continue
        file = pd.read_csv(file_path)
        for i in range(len(file)):
            insert_information(file.iloc[i], conn, cursor, table_name)


def insert_information(info, conn, cursor, table_name):
    try:
        columns = get_columns(table_name, cursor)
        placeholders = ",".join(["?"] * len(columns))

        s = f"""INSERT INTO {table_name} ({",".join(columns)}) 
          VALUES ({placeholders})"""

        values = [info[col] for col in columns]
        cursor.execute(s, values)
        conn.commit()
    except Exception as e:
        raise ValueError(f"Error: {e}")


def main():
    conn, cursor = create_connection()
    read_csv(conn, cursor)
    conn.close()


if __name__ == "__main__":
    main()
