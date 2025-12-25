import mysql.connector
from flask import current_app

def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DB']
    )

from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def create_user(name, email, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        hashed_password = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, email, password FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return User(result[0], result[1], result[2], result[3])
        return None    


class Task:
    def __init__(self, id, user_id, title, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.created_at = created_at

    @staticmethod
    def create_task(user_id, title):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (user_id, title) VALUES (%s, %s)",
            (user_id, title)
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def get_tasks_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, user_id, title, created_at FROM tasks WHERE user_id = %s",
            (user_id,)
        )
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append(Task(row[0], row[1], row[2], row[3]))
        return tasks

    @staticmethod
    def delete_task(task_id, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = %s AND user_id = %s",
            (task_id, user_id)
        )
        conn.commit()

        cursor.close()
        conn.close()        