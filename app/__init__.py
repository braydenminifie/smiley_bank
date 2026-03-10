from flask import Flask
from .routes import home_blueprint
from .database import init_db, session

def create_app():
    app = Flask(__name__)

    #Register blueprints
    app.register_blueprint(home_blueprint)

    #Create the database
    init_db()

    #Remove database session on app shut-down
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    return app