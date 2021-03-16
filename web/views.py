from flask import Blueprint, render_template, url_for, redirect

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

@mod.route('/bikes')
def bikes():
    return render_template("bikes.html")

@mod.route('/resume')
@mod.route('/resume.pdf')
def resume():
    return redirect(url_for('static', filename='rouly_resume.pdf'))
