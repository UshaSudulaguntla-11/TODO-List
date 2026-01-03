from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "todo-secret"

def get_db():
    con = sqlite3.connect("todo.db")
    con.row_factory = sqlite3.Row
    return con

@app.route("/")
def index():
    con = get_db()
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

    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    con.close()

    now = datetime.now()
    active_tasks = []
    completed_tasks = []

    for row in rows:
        due_datetime = None
        time_left_text = "No deadline"
        minutes_left = 999999

        if row["due_date"] and row["due_time"]:
            due_datetime = datetime.strptime(
                row["due_date"] + " " + row["due_time"],
                "%Y-%m-%d %H:%M"
            )

            diff_seconds = int((due_datetime - now).total_seconds())
            minutes_left = diff_seconds // 60

            if diff_seconds < 0:
                time_left_text = "Overdue"
            else:
                days = diff_seconds // 86400
                hours = (diff_seconds % 86400) // 3600
                time_left_text = f"{days} days {hours} hrs left"

        task_data = {
            "id": row["id"],
            "task": row["task"],
            "due_date": row["due_date"],
            "due_time": row["due_time"],
            "time_left": minutes_left,
            "time_left_text": time_left_text
        }

        if row["completed"]:
            completed_tasks.append(task_data)
        else:
            active_tasks.append(task_data)

    return render_template(
        "index.html",
        tasks=active_tasks,
        completed=completed_tasks
    )

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    due_date = request.form["due_date"]
    due_time = request.form["due_time"]

    due_dt = datetime.strptime(due_date + " " + due_time, "%Y-%m-%d %H:%M")
    if due_dt < datetime.now():
        flash("❌ Cannot add past date/time", "error")
        return redirect(url_for("index"))

    con = get_db()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO tasks (task, due_date, due_time) VALUES (?, ?, ?)",
        (task, due_date, due_time)
    )
    con.commit()
    con.close()

    flash("✅ Task added", "success")
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>")
def toggle(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT completed FROM tasks WHERE id=?", (id,))
    current = cur.fetchone()["completed"]
    cur.execute("UPDATE tasks SET completed=? WHERE id=?", (0 if current else 1, id))
    con.commit()
    con.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run( debug=True)











