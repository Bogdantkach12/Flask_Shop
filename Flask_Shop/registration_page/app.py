import flask

registration_page = flask.Blueprint(
    name = "registration",
    import_name = "app",
    static_folder = "static/registration_page",
    template_folder = "registration_page/templates"
)