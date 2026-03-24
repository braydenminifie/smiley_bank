from flask import Flask, render_template, Blueprint, request, jsonify
from . import services as services
from app.database import Student, Prize, History
from werkzeug.utils import secure_filename
import os

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    list_of_students = services.get_students()
    list_of_prizes = services.get_prizes()
    list_of_history = services.get_history()
    return render_template('home.html', students = list_of_students, prizes = list_of_prizes, history = list_of_history)

@home_blueprint.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    colour = data.get('colour')

    student = Student(None, name, 0, colour)
    services.add_student(student)

    history = History(None, student.student_id, services.get_date(), student.name, "Profile Added", None)
    services.add_history(history)

    return jsonify({
        "student_id": student.student_id,
        "name": student.name,
        "bank_colour": student.bank_colour,
        "smiles": student.smiles,
        "history": {
                "history_id": history.history_id,
                "student_id": history.student_id,
                "date": history.date,
                "name": history.name,
                "action": history.action,
                "points": history.points,
                    }
    })

@home_blueprint.route("/add_point/<int:student_id>", methods=["POST"])
def add_point(student_id):
    services.add_smiles(student_id, 1)
    student = services.get_student_by_id(student_id)[0]

    history = History(None, student_id, services.get_date(), student.name, "Add", 1)
    history = services.add_history(history)

    return jsonify({"points": student.smiles,
                    "history": {
                        "history_id": history.history_id,
                        "student_id": history.student_id,
                        "date": history.date,
                        "name": history.name,
                        "action": history.action,
                        "points": history.points,
                    }})

@home_blueprint.route("/remove_point/<int:student_id>", methods=["POST"])
def remove_point(student_id):
    services.remove_smiles(student_id, 1)
    student = services.get_student_by_id(student_id)[0]

    history = History(None, student_id, services.get_date(), student.name, "Remove", 1)
    history = services.add_history(history)

    return jsonify({
        "student_id": student.student_id,
        "points": student.smiles,
        "history": {
                    "history_id": history.history_id,
                    "student_id": history.student_id,
                    "date": history.date,
                    "name": history.name,
                    "action": history.action,
                    "points": history.points,
                }})
  

@home_blueprint.route("/remove_student/<int:student_id>", methods = ["POST"])
def remove_student(student_id):
    student = services.get_student_by_id(student_id)[0]
    history = History(None, student_id, services.get_date(), student.name, "Profile Removed", None)
    services.add_history(history)
    services.remove_student_by_id(student_id)


    return jsonify({
        "student_id": student_id,
        "history": {
                "history_id": history.history_id,
                "student_id": history.student_id,
                "date": history.date,
                "name": history.name,
                "action": history.action,
                "points": history.points,
                    }
    })

@home_blueprint.route("/remove_prize/<int:prize_id>", methods = ["POST"])
def remove_prize(prize_id):
    services.remove_prize(prize_id)
    return jsonify({
        "prize_id": prize_id,
    })

@home_blueprint.route('/add_prize', methods=['POST'])
def add_prize():
    prize_name = request.form.get('prizeNameInput')
    prize_cost = request.form.get('prizeCostInput')
    file = request.files.get('prizeImageUpload')

    filename = secure_filename(file.filename)
    prize = Prize(None, prize_name, prize_cost, filename)
    print(prize)

    folder = "app/static/prizes"
    os.makedirs(folder, exist_ok=True)
    file.save(os.path.join(folder, filename))

    services.add_prize(prize)

    return jsonify({
        "prize_id": prize.prize_id,
        "prize": prize.prize,
        "cost": prize.cost,
        "image": prize.image,
    })