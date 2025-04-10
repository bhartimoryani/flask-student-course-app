from flask import Blueprint, jsonify, request

from app import db
from app.models.course import Course
from app.schemas.course_schema import CourseSchema

course_bp = Blueprint('course_bp', __name__, url_prefix='/api/courses')
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

@course_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    course = course_schema.load(data)
    db.session.add(course)
    db.session.commit()
    return course_schema.jsonify(course), 201

@course_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return courses_schema.jsonify(courses)
