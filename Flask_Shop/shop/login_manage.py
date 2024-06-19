import flask_login
from .settings import shop_app
from registration_page.models import User

shop_app.secret_key = "key"

login_manager = flask_login.LoginManager(app= shop_app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)