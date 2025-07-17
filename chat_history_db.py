import sqlite3
from datetime import datetime
import os

DB_NAME = "chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            sender TEXT,
            message TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_message(session_id, sender, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO conversation_history (session_id, sender, message, timestamp)
        VALUES (?, ?, ?, ?)
    """, (session_id, sender, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_history(session_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT sender, message, timestamp FROM conversation_history
        WHERE session_id = ?
        ORDER BY id ASC
    """, (session_id,))
    history = cursor.fetchall()
    conn.close()
    return history

def export_history_to_txt(session_id, folder="chat_logs"):
    history = get_history(session_id)
    
    if not history:
        print(f"No history found for session ID: {session_id}")
        return

    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"chat_{session_id}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        for sender, message, timestamp in history:
            f.write(f"[{timestamp}] {sender}: {message}\n")

    print(f"Chat history saved to '{filename}'")
