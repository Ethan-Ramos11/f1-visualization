from flask import Blueprint, jsonify, request
from database.create_tables import create_connection, validate_connection
import sqlite3

drivers_bp = Blueprint('drivers', __name__)


@drivers_bp.route('/', methods=['GET'])
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


@drivers_bp.route('/<driver_id>', method=['GET'])
def get_driver_by_id(driver_id):
    conn, cursor = create_connection()
    if not validate_connection(conn):
        return jsonify({
            'status': 'Error',
            'message': 'Database connection failed',
            'data': None
        }), 500
    try:
        query = "SELECT * FROM drivers WHERE driver_id = ?"
        cursor.execute(query, (driver_id,))
        driver = cursor.fetchone()
        if driver:
            return jsonify({
                'status': 'success',
                'message': 'Driver found',
                'data': driver
            }), 200
        else:
            return jsonify({
                'status': 'Error',
                'message': 'Driver not found',
                'data': None
            }), 404
    except sqlite3.Error as e:
        return jsonify({
            'status': 'error',
            'message': f'Database error: {e}',
            'data': None
        }), 500
    finally:
        conn.close()


@drivers_bp.route('/search', methods=['GET'])
def search_drivers_by_name():
    conn, cursor = create_connection()
    if not validate_connection(conn):
        return jsonify({
            'status': 'Error',
            'message': 'Database connection failed',
            'data': None
        }), 500
    try:
        first_name = request.args.get('first_name', '')
        last_name = request.args.get('last_name', '')
        if not first_name or not last_name:
            return jsonify({
                'status': 'error',
                'message': 'Both first and last name required',
                'data': None
            }), 400
        query = """SELECT * FROM drivers 
                WHERE drivers.first_name LIKE ? AND drivers.last_name LIKE ?"""
        cursor.execute(query, (f'%{first_name}%', f'%{last_name}%'))
        driver_info = cursor.fetchone()
        if driver_info:
            return jsonify({
                'status': 'success',
                'message': f'{first_name} {last_name} info found',
                'data': driver_info
            }), 200
        else:
            return jsonify({
                'status': 'Error',
                'message': 'Driver info not found',
                'data': None
            }), 404
    except sqlite3.Error as e:
        return jsonify({
            'status': 'error',
            'message': f'Database error: {e}',
            'data': None
        }), 500
    finally:
        conn.close()


@drivers_bp.route('/filter', methods=['GET'])
def filter_drivers():
    pass


@drivers_bp.route('/<driver_id>/stats', methods=['GET'])
def get_driver_stats(driver_id):
    pass


@drivers_bp.route('/<driver_id>/teams', methods=['GET'])
def get_driver_teams(driver_id):
    pass


@drivers_bp.route('/compare', methods=['GET'])
def compare_drivers():
    pass


@drivers_bp.route('/standings', methods=['GET'])
def get_driver_standings():
    pass


@drivers_bp.route('/<driver_id>/current-team', methods=['GET'])
def get_driver_current_team(driver_id):
    pass


@drivers_bp.route('/<driver_id>/races', methods=['GET'])
def get_driver_races(driver_id):
    pass


@drivers_bp.route('/<driver_id>/podiums', methods=['GET'])
def get_driver_podiums(driver_id):
    pass


@drivers_bp.route('/<driver_id>/first-win', methods=['GET'])
def get_driver_first_win(driver_id):
    pass


@drivers_bp.route('/<driver_id>/championships', methods=['GET'])
def get_driver_championships(driver_id):
    pass


@drivers_bp.route('/<driver_id>/vs/<other_driver_id>', methods=['GET'])
def compare_head_to_head(driver_id, other_driver_id):
    pass


@drivers_bp.route('/<driver_id>/teammates', methods=['GET'])
def get_driver_teammates(driver_id):
    pass
