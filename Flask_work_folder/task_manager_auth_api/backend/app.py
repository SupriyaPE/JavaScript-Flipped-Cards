from flask import Flask, render_template
from config import Config
from extensions import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    jwt.init_app(app)
    # login_manager.init_app(app)

    # ---------------------------
    # FRONTEND ROUTES (ADD THESE)
    # ---------------------------

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/login")
    def login_page():
        return render_template("login.html")

    @app.route("/register")
    def register_page():
        return render_template("register.html")

    @app.route("/dashboard")
    def dashboard_page():
        return render_template("dashboard.html")

    @app.route("/tasks")
    def tasks_page():
        return render_template("tasks.html")

    # ---------------------------
    # BACKEND API BLUEPRINTS
    # ---------------------------
    from auth.routes import auth_bp
    from api.routes import api_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)