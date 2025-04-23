import sqlite3
from schema import SCHEMA


def create_connection():
    conn = sqlite3.connect('f1_info.db')
    cursor = conn.cursor()
    return conn, cursor


def convert_to_sql_columns(info):
    s = ""
    for key, val in info.items():
        s += f"{key} {val},"
    return s[:-1]


def convert_to_foreign_keys(info):
    s = ""
    for key, val in info["foreign_keys"].items():
        s += f"FOREIGN KEY ({key}) REFERENCES {val},"
    return s[:-1]


def get_columns(table_name, cursor):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]
    return columns 


def create_tables(conn, cursor):
    for table, info in SCHEMA.items():
        columns = convert_to_sql_columns(info["columns"])
        foreign_keys = ""
        if "foreign_keys" in info:
            foreign_keys = ", " + convert_to_foreign_keys(info)
        s = f"""CREATE TABLE IF NOT EXISTS {table}
          ({columns}{foreign_keys})"""
        try:
            cursor.execute(s)
            conn.commit()
        except Exception as e:
            print(f"Exception: {e}")


def main():
    conn, cursor = create_connection()
    create_tables(conn, cursor)
    conn.close()


if __name__ == "__main__":
    main()
