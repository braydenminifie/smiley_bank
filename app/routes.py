from flask import Flask, render_template, Blueprint
from . import services as services

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    list_of_students = services.get_students()
    print(list_of_students)
    return render_template('home.html', students = list_of_students)