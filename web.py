from flask import Flask, render_template

#####################
# Application Setup #
#####################

app = Flask(__name__)


###########
# Routing #
###########

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/work')
def work():
    return render_template("work.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/research')
def research():
    return render_template("research.html")

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

