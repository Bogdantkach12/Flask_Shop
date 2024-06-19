import flask 
import flask_sqlalchemy
import flask_migrate
import os

shop_app = flask.Flask(
    import_name = 'settings', 
    template_folder= 'shop/templates',
    instance_path= os.path.abspath(__file__ + '/..')
)

shop_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE = flask_sqlalchemy.SQLAlchemy(app = shop_app)

MIGRATE = flask_migrate.Migrate(app = shop_app, db = DATABASE)