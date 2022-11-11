from flask import Flask, render_template, request, url_for, redirect
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
import os

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
login = LoginManager()
moment = Moment()

if os.environ.get('FLASK_DEBUG'):
    cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        home = 'Hello'
        posts = Post.query.all()
        posts = sorted(posts, key=lambda x: x.created_on, reverse=True)
        return render_template('index.html.j2', home=home, posts=posts)


    return app

from app import models
from .models import Post