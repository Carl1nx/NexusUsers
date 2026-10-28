import os
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Nexus.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()