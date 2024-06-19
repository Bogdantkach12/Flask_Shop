import flask
import flask_login
from registration_page.models import User
def show_home_page():
    user = User.query.all()
    for users in user:
            flask_login.login_user(users)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list="home.html")
    else:
        if flask_login.current_user.is_authenticated:
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            return flask.render_template(template_name_or_list="home.html", name = name, name2 = name2, is_admin = is_admin)
