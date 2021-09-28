from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma

def create_app():
    #configure the app
    app = Flask(__name__)
    
    #configure the sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crudzin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #configure db and serializer
    config_db(app)
    config_ma(app)

    #delivery a migration
    Migrate(app, app.db) 

    #register blueprint
    from .books import bp_books
    app.register_blueprint(bp_books)
    
    return app
'''
def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crudzin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db) 

    from .books import bp_books
    app.register_blueprint(bp_books)

    return app
'''