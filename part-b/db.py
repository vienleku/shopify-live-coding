"""SQLite helpers for Part B. Provided — you don't need to change this.

`get_db()` guarantees the schema exists on every connection, so state can be
reset freely (e.g. by deleting orders.db) without breaking the endpoint.
"""
import sqlite3

DB_PATH = "orders.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
    id TEXT PRIMARY KEY,
    order_number TEXT,
    email TEXT,
    total_price TEXT,
    processed_at TEXT
)
"""


def get_db() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute(SCHEMA)  # idempotent — ensures the table exists
    return con


def init_db() -> None:
    con = get_db()
    con.commit()
    con.close()
