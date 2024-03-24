import os
import dotenv
import psycopg
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv.load_dotenv(BASE_DIR / ".env")


class PgDatabase():
    """PostgreSQL Database context manager"""

    def __init__(self) -> None:
        self.driver = psycopg

    def connect_to_database(self):
        return self.driver.connect(
            os.getenv("DATABASE_URL")
        )

    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()
