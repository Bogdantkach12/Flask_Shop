import flask
from .models import User
from shop.settings import DATABASE

def render():
    if flask.request.method == 'POST':
        print(flask.request.form)
        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            password_confirmation = flask.request.form['password_confirmation'],
            is_admin = flask.request.form['is_admin']
        )
        try:
            if user.password == user.password_confirmation:
                DATABASE.session.add(user)
                DATABASE.session.commit()
            else:
                return 'ERROR'
        except:
            return 'ERROR'
        
    return flask.render_template(template_name_or_list="registration.html")