#auth_utils.py
import sqlite3
import hashlib
from pathlib import Path
from typing import Tuple

DB_PATH = Path(__file__).resolve().parent / "users.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    with _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                password_hash TEXT NOT NULL
            )
        """)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _normalize_username(username: str) -> str:
    return " ".join(username.strip().split())


def create_user(username: str, password: str) -> bool:
    uname = _normalize_username(username)
    try:
        with _connect() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (uname, hash_password(password))
            )
        return True
    except sqlite3.IntegrityError:
        return False


def validate_user(username: str, password: str) -> bool:
    uname = _normalize_username(username)
    with _connect() as conn:
        row = conn.execute(
            "SELECT password_hash FROM users WHERE username = ? COLLATE NOCASE",
            (uname,)
        ).fetchone()
    return bool(row and row[0] == hash_password(password))


def user_exists(username: str) -> bool:
    uname = _normalize_username(username)
    with _connect() as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE username = ? COLLATE NOCASE",
            (uname,)
        ).fetchone()
    return bool(row)


def db_info() -> Tuple[str, int]:
    with _connect() as conn:
        row = conn.execute("SELECT COUNT(*) FROM users").fetchone()
        cnt = row[0] if row else 0
    return (str(DB_PATH), int(cnt))
