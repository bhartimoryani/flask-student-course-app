from flask import Blueprint, redirect, render_template, url_for

from app import db
from app.forms import StudentForm
from app.models.student import Student

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@main_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data, email=form.email.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main_bp.index'))
    return render_template('add_student.html', form=form)
