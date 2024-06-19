from registration_page import registration_page, render
from .settings import shop_app
from home_page import home, show_home_page
from login_page import log_app, show_log_page
from shop_page import shop, show_shop_page
from cart_page import cart, show_cart_page
from admin_page import admin, show_admin_page

home.add_url_rule(rule= '/', view_func= show_home_page, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint=home)
#
registration_page.add_url_rule(rule= '/registration/', view_func= render, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint= registration_page)

log_app.add_url_rule(rule= '/login/', view_func= show_log_page, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint= log_app)

shop.add_url_rule(rule= '/shop/', view_func= show_shop_page, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint=shop)

cart.add_url_rule(rule= '/cart/', view_func= show_cart_page, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint=cart)

admin.add_url_rule(rule= '/admin/', view_func= show_admin_page, methods = ['GET', 'POST'])
shop_app.register_blueprint(blueprint=admin)