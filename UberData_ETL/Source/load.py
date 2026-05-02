from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import DB_CONFIG

class Load:

    def __init__(self):
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_CONFIG['user'],
            password=DB_CONFIG['password'], 
            host=DB_CONFIG['host'],
            port=int(DB_CONFIG['port']),
            database=DB_CONFIG['database']
        )

        self.engine = create_engine(url)

    def run(self, df):
        df.to_sql("uber_data", self.engine, if_exists="replace", index=False)
        print("Data Loaded to PostgreSQL")