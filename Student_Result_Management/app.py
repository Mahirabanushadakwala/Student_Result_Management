from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    message = ""

    if request.method == "POST":

        roll = request.form["roll"]
        name = request.form["name"]
        math = request.form["math"]
        science = request.form["science"]
        english = request.form["english"]

        connection = sqlite3.connect("database.db")

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO students
                (roll,name,math,science,english)
                VALUES(?,?,?,?,?)
                """,
                (roll,name,math,science,english)
            )

            connection.commit()

            message = "Student Added Successfully!"

        except sqlite3.IntegrityError:

            message = "Roll Number Already Exists!"

        connection.close()

    return render_template("add_student.html", message=message)
    
@app.route("/view_students")
def view_students():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return render_template(
        "view_students.html",
        students=students
    )

@app.route("/search_student", methods=["GET", "POST"])
def search_student():

    student = None

    if request.method == "POST":

        roll = request.form["roll"]

        connection = sqlite3.connect("database.db")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll=?",
            (roll,)
        )

        student = cursor.fetchone()

        connection.close()

    return render_template(
        "search_student.html",
        student=student
    )

@app.route("/update_student", methods=["GET","POST"])
def update_student():

    message = ""

    if request.method == "POST":

        roll = request.form["roll"]
        math = request.form["math"]
        science = request.form["science"]
        english = request.form["english"]

        connection = sqlite3.connect("database.db")

        cursor = connection.cursor()

        cursor.execute("""
        UPDATE students
        SET math=?,
            science=?,
            english=?
        WHERE roll=?
        """,
        (math, science, english, roll))

        connection.commit()

        if cursor.rowcount > 0:
            message = "Student Updated Successfully!"
        else:
            message = "Student Not Found!"

        connection.close()

    return render_template(
        "update_student.html",
        message=message
    )

@app.route("/delete_student", methods=["GET","POST"])
def delete_student():

    message = ""

    if request.method == "POST":

        roll = request.form["roll"]

        connection = sqlite3.connect("database.db")

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE roll=?",
            (roll,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            message = "Student Deleted Successfully!"
        else:
            message = "Student Not Found!"

        connection.close()

    return render_template(
        "delete_student.html",
        message=message
    )

@app.route("/statistics")
def statistics():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("""
        SELECT AVG((math + science + english)/3.0)
        FROM students
    """)
    average = cursor.fetchone()[0]

    cursor.execute("""
        SELECT name
        FROM students
        ORDER BY rowid DESC
        LIMIT 1
    """)
    last = cursor.fetchone()

    last_student = last[0] if last else "No Student"

    connection.close()

    return render_template(
        "statistics.html",
        total_students=total_students,
        average=round(average or 0, 2),
        last_student=last_student
    )
    
@app.route("/topper")
def topper():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *,
        ((math + science + english)/3.0) AS percentage
        FROM students
        ORDER BY percentage DESC
        LIMIT 1
    """)

    topper = cursor.fetchone()

    connection.close()

    percentage = round(topper[5], 2) if topper else 0

    return render_template(
        "topper.html",
        topper=topper,
        percentage=percentage
    )
    
@app.route("/calculate_result", methods=["GET","POST"])
def calculate_result():

    student = None
    total = 0
    percentage = 0
    grade = ""

    if request.method == "POST":

        roll = request.form["roll"]

        connection = sqlite3.connect("database.db")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll=?",
            (roll,)
        )

        student = cursor.fetchone()

        connection.close()

        if student:

            total = student[2] + student[3] + student[4]
            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

    return render_template(
        "calculate_result.html",
        student=student,
        total=total,
        percentage=round(percentage, 2),
        grade=grade
    )
if __name__ == "__main__":
    app.run(debug=True)