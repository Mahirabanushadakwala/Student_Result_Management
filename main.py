def menu():
    print("\n===== Student Result Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Calculate Result")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Count Total Students")
    print("8. Show Topper")
    print("9. Class Average")
    print("10. Sort Students")
    print("11. Exit")
    

def valid_roll():
    while True:
        roll = input("Enter Roll Number: ")

        if roll == "":
            print("Roll Number cannot be empty!")
        elif not roll.isdigit():
            print("Roll Number must contain only numbers!")
        else:
            return roll


def valid_name():
    while True:
        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty!")
        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters!")
        else:
            return name


def valid_marks(subject):
    while True:
        marks = input(f"Enter {subject} Marks: ")

        if not marks.isdigit():
            print("Please enter numbers only!")

        elif int(marks) < 0 or int(marks) > 100:
            print("Marks must be between 0 and 100!")

        else:
            return marks

def add_student():
    roll = valid_roll()
    name = valid_name()
    math = valid_marks("Math")
    science = valid_marks("Science")
    english = valid_marks("English") 

    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        for line in students:
            student = line.strip().split(",")

            if student[0] == roll:
                print("Roll Number Already Exists!")
                return

    except FileNotFoundError:
        pass

    file = open("students.txt", "a")
    file.write(f"{roll},{name},{math},{science},{english}\n")
    file.close()

    print("Student Added Successfully!")
    
def view_students():
    try:
        file = open("students.txt", "r")

        data = file.readlines()

        if len(data) == 0:
            print("No student records found.")
        else:
            print("\n===== Student Records =====")

            for line in data:
                student = line.strip().split(",")

                print("--------------------------")
                print("Roll No :", student[0])
                print("Name    :", student[1])
                print("Math    :", student[2])
                print("Science :", student[3])
                print("English :", student[4])

            print("--------------------------")

        file.close()

    except FileNotFoundError:
        print("students.txt file not found!")
        
def update_marks():
    roll = input("Enter Roll Number to Update: ")

    file = open("students.txt", "r")
    students = file.readlines()
    file.close()

    found = False

    file = open("students.txt", "w")

    for line in students:
        student = line.strip().split(",")

        if student[0] == roll:
            found = True

            print("\nStudent Found")
            print("Name :", student[1])

            math = input("Enter New Math Marks: ")
            science = input("Enter New Science Marks: ")
            english = input("Enter New English Marks: ")

            file.write(f"{roll},{student[1]},{math},{science},{english}\n")

            print("Marks Updated Successfully!")

        else:
            file.write(line)

    file.close()

    if found == False:
        print("Student Not Found!")
        
def calculate_result():
    roll = input("Enter Roll Number: ")

    file = open("students.txt", "r")
    students = file.readlines()
    file.close()

    found = False

    for line in students:
        student = line.strip().split(",")

        if student[0] == roll:
            found = True

            math = int(student[2])
            science = int(student[3])
            english = int(student[4])

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
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "Fail"

            print("\n===== Student Result =====")
            print("Roll No    :", student[0])
            print("Name       :", student[1])
            print("Math       :", math)
            print("Science    :", science)
            print("English    :", english)
            print("---------------------------")
            print("Total      :", total)
            print("Percentage :", round(percentage, 2), "%")
            print("Grade      :", grade)
            print("===========================")

    if found == False:
        print("Student Not Found!")
        
def search_student():
    roll = input("Enter Roll Number to Search: ")

    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        found = False

        for line in students:
            student = line.strip().split(",")

            if student[0] == roll:
                found = True

                print("\n===== Student Found =====")
                print("Roll No  :", student[0])
                print("Name     :", student[1])
                print("Math     :", student[2])
                print("Science  :", student[3])
                print("English  :", student[4])
                print("==========================")

                break

        if found == False:
            print("Student Not Found!")

    except FileNotFoundError:
        print("students.txt file not found!")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        found = False

        file = open("students.txt", "w")

        for line in students:
            student = line.strip().split(",")

            if student[0] == roll:
                found = True
                print("Student Deleted Successfully!")
            else:
                file.write(line)

        file.close()

        if found == False:
            print("Student Not Found!")

    except FileNotFoundError:
        print("students.txt file not found!")

def count_students():
    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        total = len(students)

        if total == 0:
            print("No Student Records Found!")
            return

        # Get last student
        last_student = students[-1].strip().split(",")

        print("\n===== Student Statistics =====")
        print("Total Students :", total)
        print("Last Student Added :", last_student[1])
        print("==============================")

    except FileNotFoundError:
        print("students.txt file not found!")
        
def show_topper():
    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        if len(students) == 0:
            print("No Student Records Found!")
            return

        highest = 0
        topper = None

        for line in students:
            student = line.strip().split(",")

            math = int(student[2])
            science = int(student[3])
            english = int(student[4])

            total = math + science + english
            percentage = total / 3

            if percentage > highest:
                highest = percentage
                topper = student

        print("\n========== TOPPER ==========")
        print("Roll No    :", topper[0])
        print("Name       :", topper[1])
        print("Math       :", topper[2])
        print("Science    :", topper[3])
        print("English    :", topper[4])
        print("----------------------------")
        print("Percentage :", round(highest, 2), "%")

        if highest >= 90:
            grade = "A+"
        elif highest >= 80:
            grade = "A"
        elif highest >= 70:
            grade = "B"
        elif highest >= 60:
            grade = "C"
        elif highest >= 50:
            grade = "D"
        else:
            grade = "Fail"

        print("Grade      :", grade)
        print("============================")

    except FileNotFoundError:
        print("students.txt file not found!")
        
def class_average():
    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        if len(students) == 0:
            print("No Student Records Found!")
            return

        total_math = 0
        total_science = 0
        total_english = 0

        for line in students:
            student = line.strip().split(",")

            total_math += int(student[2])
            total_science += int(student[3])
            total_english += int(student[4])

        total_students = len(students)

        math_avg = total_math / total_students
        science_avg = total_science / total_students
        english_avg = total_english / total_students

        overall_avg = (math_avg + science_avg + english_avg) / 3

        print("\n======= CLASS AVERAGE =======")
        print("Math Average     :", round(math_avg, 2))
        print("Science Average  :", round(science_avg, 2))
        print("English Average  :", round(english_avg, 2))
        print("------------------------------")
        print("Overall Average  :", round(overall_avg, 2))
        print("==============================")

    except FileNotFoundError:
        print("students.txt file not found!")
        
def sort_students():
    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        if len(students) == 0:
            print("No Student Records Found!")
            return

        print("\n===== SORT STUDENTS =====")
        print("1. Sort by Roll Number")
        print("2. Sort by Name")
        print("3. Sort by Percentage")

        choice = input("Enter Choice: ")

        data = []

        for line in students:
            student = line.strip().split(",")
            data.append(student)

        if choice == "1":
            data.sort(key=lambda x: int(x[0]))

        elif choice == "2":
            data.sort(key=lambda x: x[1].lower())

        elif choice == "3":
            data.sort(
                key=lambda x: (int(x[2]) + int(x[3]) + int(x[4])) / 3,
                reverse=True
            )

        else:
            print("Invalid Choice!")
            return

        print("\n===== STUDENT LIST =====")

        for student in data:
            total = int(student[2]) + int(student[3]) + int(student[4])
            percentage = total / 3

            print("----------------------------")
            print("Roll No    :", student[0])
            print("Name       :", student[1])
            print("Math       :", student[2])
            print("Science    :", student[3])
            print("English    :", student[4])
            print("Percentage :", round(percentage, 2), "%")

    except FileNotFoundError:
        print("students.txt file not found!")


while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
     add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        calculate_result()
        
    elif choice == "5":
        search_student()

    elif choice == "6":
        delete_student()
        
    elif choice == "7":
        count_students()

    elif choice == "8":
        show_topper()
    
    elif choice == "9":
        class_average()

    elif choice == "10":
        sort_students()

    elif choice == "11":
        print("Thank You for Using the System!")
    break
            
else:
    print("Invalid")


   


     