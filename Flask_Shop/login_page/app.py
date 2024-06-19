import flask

log_app = flask.Blueprint(
    name="log_app",
    import_name="app",
    template_folder= "login_page/templates"
)