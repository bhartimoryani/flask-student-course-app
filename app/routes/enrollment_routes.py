from flask import Blueprint, jsonify, request

from app import db
from app.models.enrollment import Enrollment
from app.schemas.enrollment_schema import EnrollmentSchema

enrollment_bp = Blueprint('enrollment_bp', __name__, url_prefix='/api/enrollments')
enrollment_schema = EnrollmentSchema()
enrollments_schema = EnrollmentSchema(many=True)

@enrollment_bp.route('/', methods=['POST'])
def create_enrollment():
    data = request.get_json()
    enrollment = enrollment_schema.load(data)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment_schema.jsonify(enrollment), 201

@enrollment_bp.route('/', methods=['GET'])
def get_enrollments():
    enrollments = Enrollment.query.all()
    return enrollments_schema.jsonify(enrollments)
