from datetime import timedelta
from flask import Flask, render_template
from flask_minify import Minify
from werkzeug.middleware.proxy_fix import ProxyFix

from web import views
from web.cache import cache

config = {
    "SEND_FILE_MAX_AGE_DEFAULT": timedelta(days=30),
}

# Initialize application.
app = Flask(__name__)

# Configure application.
app.config.from_mapping(config)
Minify(app=app)
cache.init_app(app)
app.register_blueprint(views.mod)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html'), 500
