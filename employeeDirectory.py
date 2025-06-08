employees = []

def display_menu():
    print("Employee Directory")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        employees.append({'name': name, 'position': position})
        print("Employee added successfully.")

    elif choice == '2':
        if not employees:
            print("No employees found.")
        else:
            for i, emp in enumerate(employees, start=1):
                print(f"{i}. {emp['name']} - {emp['position']}")

    elif choice == '3':
        search_name = input("Enter employee name to search: ")
        found = False
        for emp in employess:
            if emp['name'].lower() == search_name.lower():
                print(f"Found: {emp['name']} - {emp['position']}")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == '4':
        update_name = input("Enter employee name to update: ")
        for emp in employees:
            if emp['name'].lower() == update_name.lower():
                new_name = input("Enter new name: ")
                new_position = input("Enter new position: ")
                emp['name'] = new_name
                emp['position'] = new_position
                print("Employee updated successfully.")
                break
        else:
            print("Employee not found.")

    elif choice == '5':
        delete_name = input("Enter employee name to delete: ")
        for i, emp in enumerate(employees):
            if emp['name'].lower() == delete_name.lower():
                del employees[i]
                print("Employee deleted successfully.")
                break
        else:
            print("Employee not found.")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")