import os
import time
from flask import Flask, jsonify
import MySQLdb

app = Flask(__name__)

DB_HOST = os.getenv("MYSQL_HOST", "mysql")
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
DB_NAME = os.getenv("MYSQL_DB", "devops")

def get_db_connection(retries=15, delay=2):
    last_err = None
    for _ in range(retries):
        try:
            conn = MySQLdb.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                db=DB_NAME
            )
            return conn
        except Exception as e:
            last_err = e
            time.sleep(delay)
    raise last_err

@app.route("/")
def home():
    return "✅ Two-tier app is running (Flask + MySQL)!"

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(status="ok", mysql="connected")
    except Exception as e:
        return jsonify(status="degraded", mysql="not_connected", error=str(e)), 500

@app.route("/init-db")
def init_db():
    """
    Creates a demo table + inserts one row (safe to run multiple times).
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            msg VARCHAR(255) NOT NULL
        );
    """)
    cur.execute("INSERT INTO messages (msg) VALUES ('Hello from Jenkins CI/CD + Docker!');")
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(status="ok", message="DB initialized and sample row inserted")

@app.route("/messages")
def messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, msg FROM messages ORDER BY id DESC LIMIT 10;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(messages=[{"id": r[0], "msg": r[1]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
