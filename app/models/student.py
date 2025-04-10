from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Relationship: One student can have many enrollments
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')
