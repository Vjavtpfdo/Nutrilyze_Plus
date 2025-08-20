# auth_utils.py
import sqlite3
import hashlib

DB_PATH = "users.db"

def init_db():
    """Initialize the SQLite database with the users table."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Return a SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username: str, password: str) -> bool:
    """Create a new user with a hashed password. Returns True if successful."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username.strip(), hash_password(password))
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Username already exists
        return False

def validate_user(username: str, password: str) -> bool:
    """Check if a username/password pair is valid."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username.strip(),))
    row = cur.fetchone()
    conn.close()
    if row:
        stored_hash = row[0]
        return stored_hash == hash_password(password)
    return False

# Run only when executed directly to set up DB
if __name__ == "__main__":
    init_db()
    print("Database initialized with users table.")
