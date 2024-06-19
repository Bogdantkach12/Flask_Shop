import flask

home = flask.Blueprint(
    name = "home",
    import_name = 'app',
    template_folder = "home_page/templates"
)