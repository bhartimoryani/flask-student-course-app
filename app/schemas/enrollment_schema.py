from app import ma
from app.models.enrollment import Enrollment


class EnrollmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Enrollment
        load_instance = True

    id = ma.auto_field()
    student_id = ma.auto_field()
    course_id = ma.auto_field()
