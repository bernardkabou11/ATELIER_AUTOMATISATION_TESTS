import sqlite3
import json
import os

DB_NAME = "runs.db"

def init_db():
    """Crée la base si elle n'existe pas."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            success_rate REAL,
            avg_latency REAL,
            p95_latency REAL,
            errors INTEGER,
            functional_json TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_run(result):
    """Enregistre un run dans SQLite."""
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO runs (timestamp, success_rate, avg_latency, p95_latency, errors, functional_json)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        result["timestamp"],
        result["success_rate"],
        result["avg_latency"],
        result["p95_latency"],
        result["errors"],
        json.dumps(result["functional"])
    ))

    conn.commit()
    conn.close()

def list_runs():
    """Retourne tous les runs sous forme de liste de dictionnaires."""
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT id, timestamp, success_rate, avg_latency, p95_latency, errors, functional_json FROM runs ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()

    runs = []
    for r in rows:
        runs.append({
            "id": r[0],
            "timestamp": r[1],
            "success_rate": r[2],
            "avg_latency": r[3],
            "p95_latency": r[4],
            "errors": r[5],
            "functional": json.loads(r[6])
        })

    return runs

