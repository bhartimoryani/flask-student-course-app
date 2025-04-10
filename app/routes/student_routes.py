from flask import Blueprint, jsonify, request

from app import db
from app.models.student import Student
from app.schemas.student_schema import StudentSchema

student_bp = Blueprint('student_bp', __name__, url_prefix='/api/students')
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@student_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return students_schema.jsonify(students)

@student_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    student = student_schema.load(data)
    db.session.add(student)
    db.session.commit()
    return student_schema.jsonify(student), 201
