# Advanced To-Do App

A fullstack **To-Do application** built with **Flask** and **SQLite**, with a clean **Tailwind CSS** frontend.  
Tasks are saved in a database, so they **persist across sessions**.

---

## Features

- Add new tasks with **due date and time**
- Mark tasks as **completed**
- Delete tasks
- Tasks are color-coded based on **time left**:
  - Red = overdue
  - Yellow = less than 1 day left
  - Blue/Green = plenty of time left
- Tasks are saved in **SQLite** (`todo.db`) and persist when the app is reopened
- **Responsive UI** using Tailwind CSS

---

## Folder Structure

advanced-todo-app/
│
├── app.py # Flask backend

├── create_db.py # Generates todo.db with sample tasks

├── requirements.txt # Python dependencies

├── README.md # This file

└── templates/
└── index.html # Frontend HTML (Tailwind CSS)

Install dependencies:

pip install -r requirements.txt


Create the database with sample tasks (optional if you already have todo.db):

python create_db.py


Run the app:

python app.py


Open your browser at:

http://127.0.0.1:5000/


Usage

Add a task using the form on the right side.

Mark tasks as completed by clicking the checkbox.

Delete tasks using the red  icon.

Tasks with deadlines will show time left dynamically.



Screenshots/Demo

Screenshot:https://github.com/UshaSudulaguntla-11/TODO-List/blob/main/image.png

