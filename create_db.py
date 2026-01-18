import sqlite3
from datetime import datetime, timedelta
import os


DB_PATH = os.path.join(os.path.dirname(__file__), "todo.db")


con = sqlite3.connect(DB_PATH)
cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    due_date TEXT,
    due_time TEXT,
    completed INTEGER DEFAULT 0
)
""")

now = datetime.now()
tasks = [
    ("Buy groceries", (now + timedelta(days=1)).strftime("%Y-%m-%d"), "18:00", 0),
    ("Finish project", (now + timedelta(days=2)).strftime("%Y-%m-%d"), "12:00", 0),
    ("Call mom", (now + timedelta(days=1)).strftime("%Y-%m-%d"), "20:00", 0),
]

cur.executemany("INSERT INTO tasks (task, due_date, due_time, completed) VALUES (?, ?, ?, ?)", tasks)

con.commit()
con.close()

print("todo.db created with sample tasks!")
