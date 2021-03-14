from flask import Flask, render_template
from flask_minify import minify
from flask_gravatar import Gravatar
from web import views

app = Flask(__name__)
minify(app=app)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html'), 500

app.register_blueprint(views.mod)

gravatar = Gravatar(app,
    size=300,
    rating='g',
    default='retro',
    force_default=False,
    use_ssl=True,
    base_url=None)
