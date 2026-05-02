🚕 Uber Data ETL Pipeline

This project is a simple and scalable ETL (Extract, Transform, Load) pipeline built using Python. It processes Uber dataset files and loads the cleaned data into a PostgreSQL database using SQLAlchemy.

📌 Project Overview

The pipeline performs three main steps:

Extract – Reads raw Uber dataset
Transform – Cleans and processes the data
Load – Stores the data into PostgreSQL
🗂️ Project Structure
UberData_ETL/
│
├── Source/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│
├── config.py
├── requirements.txt
└── README.md
⚙️ Tech Stack
Python 3.x
Pandas
SQLAlchemy
psycopg2
PostgreSQL
Visual Studio Code
🚀 Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd UberData_ETL
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Setup Database

Install PostgreSQL and create a database:

CREATE DATABASE Uber_db;
5. Configure Database

Edit config.py:

DB_CONFIG = {
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
    "database": "Uber_db"
}
▶️ Run the Pipeline

From project root directory:

python -m Source.main
📊 Output
A table named uber_data will be created in PostgreSQL
Data is loaded using pandas.to_sql()
💡 Future Improvements
Add logging system
Use environment variables for credentials
Add Docker support
Schedule pipeline (Airflow / Cron)
🤝 Contribution

Feel free to fork and improve the project.

📜 License

This project is open-source and available under the MIT License.
