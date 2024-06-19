import flask

cart = flask.Blueprint(
    name = "cart",
    import_name = 'app',
    template_folder = "cart_page/templates"
)