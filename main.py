def menu():
    print("\n===== Student Result Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Calculate Result")
    print("5. Exit")


while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Student selected")

    elif choice == "2":
        print("View Students selected")

    elif choice == "3":
        print("Update Marks selected")

    elif choice == "4":
        print("Calculate Result selected")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")