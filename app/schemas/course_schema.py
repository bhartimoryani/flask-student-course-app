from app import ma
from app.models.course import Course


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Course
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
