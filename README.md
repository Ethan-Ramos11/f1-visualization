# F1 Visualization Project

A Formula 1 data visualization and analysis tool built with Flask, SQLite3, and NiceGUI. This project was created as a learning exercise to practice working with web frameworks, databases, and modern UI development while exploring Formula 1 data.

## 🏎️ Project Overview

This project combines my passion for Formula 1 with practical software development skills. It provides a comprehensive platform for exploring F1 data through a modern web interface, backed by a robust database system.

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite3 (Lightweight, file-based database)
- **Frontend**: NiceGUI (Modern Python-based UI framework)
- **Data**: Formula 1 statistics and historical data

## 🚀 Features

- Driver information and statistics
- Team performance analysis
- Historical race data
- Driver comparisons
- Championship standings
- Interactive data visualization

## 📊 API Endpoints

The project includes several RESTful API endpoints for accessing F1 data:

- `/drivers` - Get all drivers
- `/drivers/<driver_id>` - Get specific driver information
- `/drivers/search` - Search drivers by name
- `/drivers/filter` - Filter drivers by various criteria
- `/drivers/<driver_id>/team` - Get driver's current team
- `/drivers/<driver_id>/stats` - Get driver statistics
- `/drivers/compare` - Compare multiple drivers
- `/drivers/standings` - Get current championship standings

## 🏗️ Project Structure

```
f1-visualization/
├── server/
│   ├── routes/
│   │   └── drivers.py
│   ├── database/
│   │   └── create_tables.py
│   └── app.py
├── csv_data/
│   └── drivers.csv
└── README.md
```

## 🚦 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask nicegui sqlite3
   ```
3. Initialize the database:
   ```bash
   python server/database/create_tables.py
   ```
4. Run the application:
   ```bash
   python server/app.py
   ```

## 🎯 Learning Objectives

This project was created to practice and improve skills in:

- Flask web framework development
- SQLite3 database management
- RESTful API design
- Modern UI development with NiceGUI
- Data visualization
- Python programming best practices

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite3 Documentation](https://www.sqlite.org/docs.html)
- [NiceGUI Documentation](https://nicegui.io/)
- [Formula 1 Official Website](https://www.formula1.com/)

## 🤝 Contributing

Feel free to fork this project and contribute! Whether it's adding new features, improving the UI, or enhancing the database structure, all contributions are welcome.

## 📝 License

This project is open source and available under the MIT License.
