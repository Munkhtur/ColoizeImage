from flask import Flask, render_template, url_for, redirect, session
from flask_session import Session
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f2e20655a99caf9b80987a2c6428d30c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)
    app.config['SESSION_FILE_THRESHOLD'] = 100
    sess = Session()

    sess.init_app(app)

    app.static_folder = 'static'
    from app.main.routes import main
    app.register_blueprint(main)
    return app
