from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Sample data
students = [{"id": "16", "name": "Jimin"}, {"id": "17", "name": "Namjoon"}]
assignments = [{'assi': 1, 'title': 'Assignment 1'}, {'assi': 2, 'title': 'Assignment 2'}]
tests = [{'testn': 1, 'title': 'Test 1'}, {'testn': 2, 'title': 'Test 2'}]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/student')
def show_students():
    return render_template('student.html', students=students)

@app.route('/stud', methods=['POST'])
def student_main():
    if request.form['type'] == "student":
        if request.form['type'] == "student":
            students.append({'id': len(students) + 1, 'name': request.form['name']})
    return redirect(url_for('show_students'))

@app.route('/assignment')
def show_assignment():
    return render_template('assignment.html', assignments=assignments)
    
@app.route('/asg', methods=['POST'])
def assignment_main():
    if request.form['type'] == "assignment":
        assignments.append({'assi': len(assignments) + 1, 'title': request.form['title']})
    return redirect(url_for('show_assignment'))

@app.route('/test')
def show_test():
    return render_template('test.html', tests=tests)

@app.route('/tes', methods=['POST'])
def test_main():
    if request.form['type'] == "test":
        tests.append({'testn': len(tests) + 1, 'title': request.form['title']})
    return redirect(url_for('show_test'))
