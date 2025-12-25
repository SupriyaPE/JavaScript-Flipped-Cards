from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "3332"
app.permanent_session_lifetime=timedelta(minutes=1)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users(email, password) VALUES (%s, %s)",
            (email, password))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("login"))
    return render_template("signup.html")   


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE email=%s",
        (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user["password"],
         password):
           session.permanent =True
           session["user"]=user["email"]
           return redirect(url_for("dashboard"))
        return "invalid credential"   
    return render_template("login.html")        


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html",user=session["user"])  


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))      


if __name__ == "__main__":
    app.run(debug=True)