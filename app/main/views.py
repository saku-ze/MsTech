from flask import render_template
from . import bp


@bp.route("/")
@bp.route("/index")
def index():
    return render_template('index.html')


@bp.route("/members")
def members():
    return render_template('members.html')


@bp.route("/project/<int:id>")
def show_project(id):
    return render_template("wedo2.html")
