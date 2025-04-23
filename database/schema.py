import os

# Define the path to the CSV files
CSV_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv_data')

# Schema definition
SCHEMA = {
    'circuits': {
        'file': 'circuits.csv',
        'columns': {
            'circuit_id': 'INTEGER PRIMARY KEY',
            'circuit_name': 'TEXT',
            'location': 'TEXT',
            'country': 'TEXT',
            'circuit_length_km': 'REAL',
            'lap_record': 'TEXT',
            'lap_record_driver': 'TEXT',
            'first_gp_year': 'INTEGER',
            'circuit_type': 'TEXT'
        }
    },
    'teams': {
        'file': 'teams.csv',
        'columns': {
            'team_id': 'INTEGER PRIMARY KEY',
            'team_name': 'TEXT',
            'nationality': 'TEXT',
            'team_principal': 'TEXT',
            'engine_supplier': 'TEXT',
            'base_location': 'TEXT',
            'constructors_championships': 'INTEGER',
            'founding_year': 'INTEGER',
            'active': 'BOOLEAN'
        }
    },
    'drivers': {
        'file': 'drivers.csv',
        'columns': {
            'driver_id': 'INTEGER PRIMARY KEY',
            'first_name': 'TEXT',
            'last_name': 'TEXT',
            'nationality': 'TEXT',
            'date_of_birth': 'TEXT',
            'team_id': 'INTEGER',
            'driver_number': 'INTEGER',
            'championships_won': 'INTEGER',
            'active': 'BOOLEAN'
        },
        'foreign_keys': {
            'team_id': 'teams(team_id)'
        }
    },
    'races': {
        'file': 'races.csv',
        'columns': {
            'race_id': 'INTEGER PRIMARY KEY',
            'race_name': 'TEXT',
            'season': 'INTEGER',
            'round': 'INTEGER',
            'circuit_id': 'INTEGER',
            'race_date': 'TEXT',
            'race_time': 'TEXT',
            'sprint_race': 'BOOLEAN'
        },
        'foreign_keys': {
            'circuit_id': 'circuits(circuit_id)'
        }
    },
    'results': {
        'file': 'results.csv',
        'columns': {
            'result_id': 'INTEGER PRIMARY KEY',
            'race_id': 'INTEGER',
            'driver_id': 'INTEGER',
            'grid_position': 'INTEGER',
            'finish_position': 'INTEGER',
            'points': 'INTEGER',
            'fastest_lap': 'BOOLEAN',
            'status': 'TEXT'
        },
        'foreign_keys': {
            'race_id': 'races(race_id)',
            'driver_id': 'drivers(driver_id)'
        }
    },
    'drivers_standings': {
        'file': 'drivers_standings.csv',
        'columns': {
            'standing_id': 'INTEGER PRIMARY KEY',
            'driver_id': 'INTEGER',
            'season': 'INTEGER',
            'points': 'INTEGER',
            'position': 'INTEGER',
            'wins': 'INTEGER'
        },
        'foreign_keys': {
            'driver_id': 'drivers(driver_id)'
        }
    },
    'constructors_standings': {
        'file': 'constructors_standings.csv',
        'columns': {
            'standing_id': 'INTEGER PRIMARY KEY',
            'team_id': 'INTEGER',
            'season': 'INTEGER',
            'points': 'INTEGER',
            'position': 'INTEGER',
            'wins': 'INTEGER'
        },
        'foreign_keys': {
            'team_id': 'teams(team_id)'
        }
    }
}
