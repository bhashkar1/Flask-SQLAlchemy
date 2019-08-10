from app import app
from flask import render_template, request
from dbSetup import Courses, new_course

@app.route('/')
def index():
    courses = Courses.query.all()
    return render_template('index.html', courses = courses)

@app.route('/new', methods=['GET','POST'])
def new():
    if request.method =='GET':
        return render_template('new.html')
    course_name = request.form.get('name_field')
    course_description = request.form.get('description_field')
    course_price = request.form.get('price_field')

    course = new_course(course_name, course_description, course_price)

    return render_template('new.html', course=course)


