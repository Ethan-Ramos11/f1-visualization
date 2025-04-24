from flask import Blueprint, jsonify
from database.create_tables import create_connection, validate_connection
import sqlite3

drivers_bp = Blueprint('drivers', __name__)


@drivers_bp.route('/')
def get_all_drivers():
    conn, cursor = create_connection()
    if not validate_connection(conn):
        return jsonify({
            'status': 'Error',
            'message': 'Database connection failed',
            'data': None
        }), 500
    try:
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
                'status': 'Error',
                'message': 'Drivers not found',
                'data': []
            }), 404
    except sqlite3.Error as e:
        return jsonify({
            'status': 'error',
            'message': f'Database error: {e}',
            'data': None
        }), 500
    finally:
        conn.close()
