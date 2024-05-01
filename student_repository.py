import json
import os

# Refactored version


def save_student_record(student, file_name="students_data.json"):
    data = load_json_file(file_name)
    unique_key = generate_unique_key(data)
    data[unique_key] = student
    write_json_file(data, file_name)
    return {unique_key: student}


def get_student_record(key, file_name="students_data.json"):
    data = load_json_file(file_name)
    return data.get(key, {"error": "Invalid Student ID!"})


def update_student_record(key, student, file_name="students_data.json"):
    data = load_json_file(file_name)
    if key in data:
        data[key] = student
        write_json_file(data, file_name)
        return {key: student}
    else:
        return {"error": "Invalid Student ID!"}


def get_all_students_record(file_name="students_data.json"):
    return load_json_file(file_name)


def delete_student_record(key, file_name="students_data.json"):
    data = load_json_file(file_name)
    if key in data:
        data.pop(key)
        write_json_file(data, file_name)
        return data
    else:
        return {"error": "Invalid Student ID!"}


def generate_unique_key(data):
    key = len(data) + 1
    while "student" + str(key) in data:
        key += 1
    return "student" + str(key)


def load_json_file(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def write_json_file(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=6)


def create_test_data_file(data, file_name="students_test_data.json"):
    write_json_file(data, file_name)


def delete_test_data_file(file_name="students_test_data.json"):
    if os.path.exists(file_name):
        os.remove(file_name)