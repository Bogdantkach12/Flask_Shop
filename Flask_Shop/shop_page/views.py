import flask
import flask_login
import registration_page
import registration_page.models
def show_shop_page():
    user = registration_page.models.User.query.all()
    for users in user:
            flask_login.login_user(users)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list="shop.html")
    else:
        if flask_login.current_user.is_authenticated:
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            return flask.render_template(template_name_or_list="shop.html", name = name, name2 = name2, is_admin = is_admin)