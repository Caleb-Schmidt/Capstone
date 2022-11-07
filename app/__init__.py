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
    moment.init_app(app)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        home = 'Hello'
        return render_template('index.html.j2', home=home)

    app.config["DEBUG"] = True

    # Upload folder
    UPLOAD_FOLDER = 'static/files'
    app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

    # Get the uploaded files
    @app.route("/", methods=['POST'])
    def uploadFiles():
        # get the uploaded file
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
            # save the file
        return redirect(url_for('index'))


    return app