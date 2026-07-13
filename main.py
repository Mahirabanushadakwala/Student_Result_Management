def menu():
    print("\n===== Student Result Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Calculate Result")
    print("5. Exit")
    
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    math = input("Enter Math Marks: ")
    science = input("Enter Science Marks: ")
    english = input("Enter English Marks: ")

    file = open("students.txt", "a")
    file.write(f"{roll},{name},{math},{science},{english}\n")
    file.close()

    print("Student added successfully!")
    
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
        print("\n=================================")
        print(" Thank You for Using the System ")
        print(" Exiting Program...")
        print("=================================")
        break

    else:
        print("Invalid Choice! Please try again.")


     