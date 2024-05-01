from flask import Flask, jsonify, request
from .student_repository import save_student_record, delete_student_record, get_student_record, update_student_record, get_all_students_record

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"app_name": "Student Records Management API", "version": "0.0.1", "author": "Ali Naqi Al-Musawi"})


@app.route("/save-student", methods=["POST",])
def save_student():
    request_body = request.get_json()
    if (request_body.get('name') == None or request_body.get('program') == None or request_body.get("department") == None):
        return jsonify({"error": "Incomplete Student Data!"})

    student = {
        "name": request_body['name'],
        "program": request_body['program'],
        "department": request_body['department'],
    }
    return (save_student_record(student)), 201


@app.route("/get-all-students")
def get_all_student():
    return (get_all_students_record()), 200


@app.route("/get-student/<studentID>")
def get_student(studentID):
    return (get_student_record(studentID)), 200


@app.route("/update-student/<studentID>", methods=["PUT"])
def update_student(studentID):
    request_body = request.get_json()
    if (request_body.get('name') == None or request_body.get('program') == None or request_body.get("department") == None):
        return jsonify({"error": "Incomplete Student Data!"})

    student = {
        "name": request_body['name'],
        "program": request_body['program'],
        "department": request_body['department'],
    }
    return (update_student_record(studentID, student)), 200


@app.route("/delete-student/<studentID>", methods=["DELETE"])
def delete_student(studentID):
    return (delete_student_record(studentID)), 200
