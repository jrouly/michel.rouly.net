from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html'), 500

from web import views
app.register_blueprint(views.mod)