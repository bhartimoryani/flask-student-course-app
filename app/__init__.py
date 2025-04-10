# app/__init__.py
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Blueprints will be registered here later
    return app
