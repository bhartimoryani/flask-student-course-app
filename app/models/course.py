from app import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Relationship: One course can have many enrollments
    enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')
