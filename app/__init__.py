from flask import Flask
from .config import Config
from .models import db
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "core.login"  # placeholder

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.core import core_bp
    app.register_blueprint(core_bp)

    with app.app_context():
        db.create_all()  # dev convenience

    return app
