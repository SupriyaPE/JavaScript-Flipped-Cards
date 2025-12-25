from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime, random, smtplib
from email.message import EmailMessage

from config import SECRET_KEY, JWT_SECRET, JWT_EXP_MINUTES, SMTP_EMAIL, SMTP_APP_PASSWORD, SMTP_SERVER, SMTP_PORT
from db import get_db_connection

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ---------------- PAGES ----------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")
  
# ---------------- Subject ----------------
def send_otp_email(to_email, otp):
    msg = EmailMessage()
    msg["Subject"] = "JioMart Signup OTP"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email
    msg.set_content(f"Your OTP is {otp}")

    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(SMTP_EMAIL, SMTP_APP_PASSWORD)
    server.send_message(msg)
    server.quit()

def token_required(token):
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return data
    except:
        return None

# ----------------------------------------------------

def cleanup_expired_otps():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT email FROM email_otp WHERE expires_at < NOW()" # Get emails where OTP is expired
    )
    expired_emails = cur.fetchall()

    for (email,) in expired_emails:

        cur.execute(                                          # Delete expired OTP
            "DELETE FROM email_otp WHERE email = %s",
            (email,)
        )

        cur.execute(                                           # Delete unverified user linked to expired OTP

            "DELETE FROM users WHERE email = %s AND is_verified = FALSE",
            (email,)
        )

    conn.commit()
    cur.close()
    conn.close(

    )
# ---------------- APIs ----------------
@app.route("/api/signup", methods=["POST"])
def signup():
    cleanup_expired_otps() 

    data = request.json
    email = data.get("email")
    password = data.get("password")

    hashed_password = generate_password_hash(password)
    otp = str(random.randint(100000, 999999))
    expiry = datetime.datetime.now() + datetime.timedelta(minutes=5)

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    if cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({"message": "Email already exists"}), 400

    cur.execute(
        "INSERT INTO users (email, password, is_verified) VALUES (%s, %s, %s)", 
        (email, hashed_password, False)
    )
    cur.execute(
        "INSERT INTO email_otp (email, otp, expires_at) VALUES (%s, %s, %s)",
        (email, otp, expiry)
    )
    conn.commit()
    cur.close()
    conn.close()

    send_otp_email(email, otp)
    return jsonify({"message": "OTP sent to email"}), 200


@app.route("/api/verify-otp", methods=["POST"])
def verify_otp():
    data = request.json
    email = data.get("email")
    otp = data.get("otp")

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    # check valid OTP
    cur.execute(
        "SELECT * FROM email_otp WHERE email=%s AND otp=%s AND expires_at > NOW()",
        (email, otp)
    )
    otp_row = cur.fetchone()

    if not otp_row:
        cur.close()
        conn.close()
        return jsonify({"message": "Invalid or expired OTP"}), 400

    # mark user as verified
    cur.execute(
        "UPDATE users SET is_verified = TRUE WHERE email = %s",
        (email,)
    )

    # get user id
    cur.execute(
        "SELECT id, email FROM users WHERE email=%s",
        (email,)
    )
    user = cur.fetchone()

    # delete OTP record
    cur.execute(
        "DELETE FROM email_otp WHERE email=%s",
        (email,)
    )
    conn.commit()
    cur.close()
    conn.close()

    # generate JWT token
    token = jwt.encode(
        {
           "user_id": user["id"],
           "email": user["email"],
           "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXP_MINUTES)
        },
        JWT_SECRET,
        algorithm="HS256"
    )

    # send token back
    return jsonify({
        "message": "Email verified",
        "token": token
    }), 200


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE email=%s AND is_verified=TRUE", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            "user_id": user["id"],
            "email": user["email"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXP_MINUTES)
        },
        JWT_SECRET,
        algorithm="HS256"
    )
    return jsonify({"token": token}), 200


@app.route("/api/dashboard", methods=["GET"])
def dashboard_api():
    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"message": "Token missing"}), 401

    token = auth.split(" ")[1]
    data = token_required(token)
    if not data:
        return jsonify({"message": "Invalid token"}), 401

    return jsonify({"message": f"Welcome {data['email']}"}), 200


if __name__ == "__main__":
    app.run(debug=True)