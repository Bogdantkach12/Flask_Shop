import flask
import flask_login

import registration_page.models

def show_log_page():
    if flask.request.method == 'POST':
        users = registration_page.models.User.query.all()
        for user in users:
            if user.login == flask.request.form['login'] and user.password == flask.request.form['password']:
                flask_login.login_user(user)
                
    is_admin = False

    if not flask_login.current_user.is_authenticated:
        return flask.render_template('login.html')
    else:
        is_admin = flask_login.current_user.is_admin
        return flask.redirect('/')
