from app import ma
from app.models.student import Student


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
