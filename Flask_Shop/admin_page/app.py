import flask

admin = flask.Blueprint(
    name = "admin",
    import_name="app",
    template_folder="admin_page/templates"
)