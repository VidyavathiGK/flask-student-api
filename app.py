from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "age": 20},
    {"id": 2, "name": "Anjali", "age": 21}
]

@app.route("/")
def home():
    return "Welcome to Flask Student API "

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    student_id = data["id"]
    students[student_id] = {
        "name": data["name"],
        "age": data["age"],
        "course": data["course"]
    }

    return jsonify({"message": "Student added successfully"}), 201


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<student_id>", methods=["PUT"])
def update_student(student_id):
    if student_id in students:
        data = request.get_json()
        students[student_id].update(data)
        return jsonify({"message": "Student updated successfully"})
    return jsonify({"error": "Student not found"}), 404


@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        return jsonify({"message": "Student deleted successfully"})
    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
