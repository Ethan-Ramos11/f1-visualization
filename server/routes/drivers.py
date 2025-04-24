from flask import Blueprint, jsonify
from database.create_tables import create_connection
import sqlite3

drivers_bp = Blueprint('drivers', __name__)


def validate_connection(conn):
    if conn == None:
        return False
    try:
        conn.execute("SELECT 1")
        return True
    except sqlite3.Error:
        return False


@drivers_bp.route('/')
def get_all_drivers():
    conn, cursor = create_connection()
    if not validate_connection(conn):
        return jsonify({
            'status': 'error',
            'message': 'Database connection failed',
            'data': None
        }), 500
    query = "SELECT * FROM drivers"
    cursor.execute(query)
    drivers = cursor.fetchall()
    if drivers:
        return jsonify({
            'status': 'success',
            'message': 'Drivers found',
            'data': drivers
        }), 200
    else:
        return jsonify({

        }), 404
