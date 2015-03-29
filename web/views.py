from flask import Blueprint, render_template

mod = Blueprint('views', __name__)

@mod.route('/')
def homepage():
    return render_template("index.html")

@mod.route('/work')
def work():
    return render_template("work.html")

@mod.route('/projects')
def projects():
    return render_template("projects.html")

@mod.route('/research')
def research():
    return render_template("research.html")

@mod.route('/community')
def community():
    return render_template("community.html")

@mod.route('/contact')
def contact():
    return render_template("contact.html")

