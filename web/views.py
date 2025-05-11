from flask import Blueprint, render_template, url_for, redirect
from web.cache import cache

mod = Blueprint('views', __name__)

@mod.route('/')
@cache.cached()
def homepage():
    return render_template("index.html")

@mod.route('/work')
@cache.cached()
def work():
    return render_template("work.html")

@mod.route('/projects')
@cache.cached()
def projects():
    return render_template("projects.html")

@mod.route('/research')
@cache.cached()
def research():
    return render_template("research.html")

@mod.route('/resume')
@mod.route('/resume.pdf')
@cache.cached()
def resume():
    return redirect(url_for('static', filename='rouly_resume.pdf'))
