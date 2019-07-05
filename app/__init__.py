from app.apps import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from app.models.base import db

toolbar = DebugToolbarExtension()
migrate = Migrate(db = db)
bcrypt = Bcrypt()

def create_app():
    # instance the app
    app = Flask(__name__)

    #enable CORS
    CORS(app)

    #set config
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')

    # set up extensions
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprint
    register_blueprint(app)
    register_plugin(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}


    app.debug = True

    return app

def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def register_plugin(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
