from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Rahul", "age": 20, "course": "BCA"},
    {"id": 2, "name": "Anjali", "age": 21, "course": "BSc"}
]

# Home Route
@app.route("/")
def home():
    return "Welcome to Flask Student API"

# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# Add new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added successfully", "student": data})

# Update student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            student["course"] = data.get("course", student["course"])
            return jsonify({"message": "Student updated successfully", "student": student})
    return jsonify({"message": "Student not found"}), 404

# Delete student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})
    return jsonify({"message": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

