import sqlite3
from pathlib import Path


def get_db_connection(db_path: str):
    #Creates and returns a SQLite database connection.
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def initialize_schema(conn, schema_path: str):
    #Executes the schema.sql file to create all tables.
    
    schema_sql = Path(schema_path).read_text()
    conn.executescript(schema_sql)
    conn.commit()
