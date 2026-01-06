from flask import Flask, render_template, request, redirect
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def show_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("tasks.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s)",
            (title, description)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")
    return render_template("add_task.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        status = request.form["status"]
        cursor.execute(
            "UPDATE tasks SET title=%s, description=%s, status=%s WHERE id=%s",
            (title, description, status, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    cursor.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit_task.html", task=task)


@app.route("/delete/<int:id>")
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)