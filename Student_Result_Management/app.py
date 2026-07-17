from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        roll = request.form["roll"]
        name = request.form["name"]
        math = request.form["math"]
        science = request.form["science"]
        english = request.form["english"]

        with open("students.txt", "a") as file:
            file.write(f"{roll},{name},{math},{science},{english}\n")

        return render_template(
            "add_student.html",
            message="Student Added Successfully!"
        )

    return render_template("add_student.html")

    
@app.route("/view_students")
def view_students():

    students = []

    try:
        file = open("students.txt", "r")

        for line in file:
            student = line.strip().split(",")
            students.append(student)

        file.close()

    except FileNotFoundError:
        pass

    return render_template("view_students.html", students=students)

@app.route("/search_student", methods=["GET", "POST"])
def search_student():

    student_data = None

    if request.method == "POST":

        roll = request.form["roll"]

        try:
            with open("students.txt", "r") as file:

                for line in file:

                    student = line.strip().split(",")

                    if student[0] == roll:
                        student_data = student
                        break

        except FileNotFoundError:
            pass

    return render_template("search_student.html", student=student_data)

@app.route("/update_student", methods=["GET", "POST"])
def update_student():

    message = ""

    if request.method == "POST":

        roll = request.form["roll"]
        math = request.form["math"]
        science = request.form["science"]
        english = request.form["english"]

        students = []

        try:

            with open("students.txt", "r") as file:

                for line in file:

                    student = line.strip().split(",")

                    if student[0] == roll:

                        student[2] = math
                        student[3] = science
                        student[4] = english

                    students.append(student)

            with open("students.txt", "w") as file:

                for student in students:

                    file.write(",".join(student) + "\n")

            message = "Student Updated Successfully!"

        except FileNotFoundError:

            message = "Student File Not Found!"

    return render_template("update_student.html", message=message)

@app.route("/delete_student", methods=["GET", "POST"])
def delete_student():

    message = ""

    if request.method == "POST":

        roll = request.form["roll"]

        students = []
        found = False

        try:

            with open("students.txt", "r") as file:

                for line in file:

                    student = line.strip().split(",")

                    if student[0] != roll:

                        students.append(student)

                    else:

                        found = True

            with open("students.txt", "w") as file:

                for student in students:

                    file.write(",".join(student) + "\n")

            if found:

                message = "Student Deleted Successfully!"

            else:

                message = "Student Not Found!"

        except FileNotFoundError:

            message = "students.txt file not found!"

    return render_template("delete_student.html", message=message)

@app.route("/statistics")
def statistics():

    total_students = 0
    last_student = "No Student"

    total_math = 0
    total_science = 0
    total_english = 0

    try:

        with open("students.txt", "r") as file:

            students = file.readlines()

        total_students = len(students)

        if total_students > 0:

            last = students[-1].strip().split(",")

            last_student = last[1]

            for line in students:

                student = line.strip().split(",")

                total_math += int(student[2])
                total_science += int(student[3])
                total_english += int(student[4])

            overall_average = (
                total_math +
                total_science +
                total_english
            ) / (total_students * 3)

        else:

            overall_average = 0

    except FileNotFoundError:

        overall_average = 0

    return render_template(
        "statistics.html",
        total_students=total_students,
        last_student=last_student,
        average=round(overall_average,2)
    )
    
@app.route("/topper")
def topper():

    topper = None
    highest_percentage = 0

    try:

        with open("students.txt", "r") as file:

            for line in file:

                student = line.strip().split(",")

                math = int(student[2])
                science = int(student[3])
                english = int(student[4])

                total = math + science + english
                percentage = total / 3

                if percentage > highest_percentage:

                    highest_percentage = percentage
                    topper = student

    except FileNotFoundError:

        pass

    return render_template(
        "topper.html",
        topper=topper,
        percentage=round(highest_percentage,2)
    )
    
@app.route("/calculate_result", methods=["GET", "POST"])
def calculate_result():

    student = None
    total = 0
    percentage = 0
    grade = ""

    if request.method == "POST":

        roll = request.form["roll"]

        try:

            with open("students.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == roll:

                        student = data

                        math = int(data[2])
                        science = int(data[3])
                        english = int(data[4])

                        total = math + science + english

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

                        break

        except FileNotFoundError:
            pass

    return render_template(
        "calculate_result.html",
        student=student,
        total=total,
        percentage=round(percentage,2),
        grade=grade
    )

if __name__ == "__main__":
    app.run(debug=True)