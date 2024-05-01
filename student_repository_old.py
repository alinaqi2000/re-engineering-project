import json
import os

# Un-refactored version


def save_student_record(student, file_name="students_data.json"):
    data = get_data(file_name)
    unique_key = generate_unique_key(data)
    data[unique_key] = student
    set_data(data, file_name)
    return {unique_key: student}


def get_student_record(key, file_name="students_data.json"):
    data = get_data(file_name)
    if data.get(key):
        return data.get(key)
    else:
        return {"error": "Invalid Student ID!"}


def update_student_record(key, student, file_name="students_data.json"):
    data = get_data(file_name)
    if data.get(key):
        data[key] = student
        set_data(data, file_name)
        return {key: student}
    else:
        return {"error": "Invalid Student ID!"}


def get_all_students_record(file_name="students_data.json"):
    return get_data(file_name)


def delete_student_record(key, file_name="students_data.json"):
    data = get_data(file_name)
    if data.get(key):
        data.pop(key)
        set_data(data, file_name)
        return data
    else:
        return {"error": "Invalid Student ID!"}


def generate_unique_key(data):
    key = len(data) + 1
    while data.get("student" + str(key)):
        key += 1
    return "student" + str(key)


def get_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def set_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=6)


def create_test_data_file(data, file_name="students_test_data.json"):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=6)
        f.close()


def delete_test_data_file(file_name="students_test_data.json"):
    if os.path.exists(file_name):
        os.remove(file_name)
