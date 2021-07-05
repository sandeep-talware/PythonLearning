
from flask import Flask


def create_app():
    app = Flask(__name__)

    from  .main import main as main_bluprint
    app.register_blueprint(main_bluprint)

    from .auth import auth as auth_bluprint
    app.register_blueprint(auth_bluprint)

    return app

