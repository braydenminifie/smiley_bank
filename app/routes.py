from flask import Flask, render_template, Blueprint, request, jsonify
from . import services as services
from app.database import Student

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    list_of_students = services.get_students()
    print(list_of_students)
    return render_template('home.html', students = list_of_students)

@home_blueprint.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    colour = data.get('colour')

    student = Student(None, name, 0, colour)
    services.add_student(student)

    return jsonify({"status": "student added"})

@home_blueprint.route("/add_point/<int:student_id>", methods=["POST"])
def add_point(student_id):
    services.add_smiles(student_id, 1)
    student = services.get_student_by_id(student_id)[0]

    return {"points": student.smiles}

@home_blueprint.route("/remove_point/<int:student_id>", methods=["POST"])
def remove_point(student_id):
    services.remove_smiles(student_id, 1)
    student = services.get_student_by_id(student_id)[0]

    return {"points": student.smiles}

@home_blueprint.route("/remove_student/<int:student_id>", methods = ["POST"])
def remove_student(student_id):
    services.remove_student_by_id(student_id)
    return {"status": "removed"}