from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


def get_input(prompt):
    return input(prompt)


def find_entity_by_id(entity_type, entity_id):
    entity = entity_type.find_by_id(entity_id)
    print(entity) if entity else print(f'{entity_type.__name__} {entity_id} not found')


def create_entity(entity_type, **kwargs):
    try:
        entity = entity_type.create(**kwargs)
        print(f'Success: {entity}')
    except Exception as exc:
        print(f"Error creating {entity_type.__name__.lower()}: {exc}")


def update_entity(entity):
    try:
        entity.update()
        print(f'Success: {entity}')
    except Exception as exc:
        print(f"Error updating {entity.__class__.__name__.lower()}: {exc}")


def delete_entity(entity):
    entity.delete()
    print(f'{entity.__class__.__name__} {entity.id} deleted')


def list_entities(entities):
    for entity in entities:
        print(entity)


def list_departments():
    list_entities(Department.get_all())


def find_department_by_name():
    name = get_input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')


def find_department_by_id():
    entity_id = get_input("Enter the department's id: ")
    find_entity_by_id(Department, entity_id)


def create_department():
    name = get_input("Enter the department's name: ")
    location = get_input("Enter the department's location: ")
    create_entity(Department, name=name, location=location)


def update_department():
    department_id = get_input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        department.name = get_input("Enter the department's new name: ")
        department.location = get_input("Enter the department's new location: ")
        update_entity(department)
    else:
        print(f'Department {department_id} not found')


def delete_department():
    department_id = get_input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        delete_entity(department)
    else:
        print(f'Department {department_id} not found')


def list_employees():
    list_entities(Employee.get_all())


def find_employee_by_name():
    name = get_input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'Employee {name} not found')


def find_employee_by_id():
    entity_id = get_input("Enter the employee's id: ")
    find_entity_by_id(Employee, entity_id)


def create_employee():
    name = get_input("Enter the employee's name: ")
    job_title = get_input("Enter the employee's job title: ")
    department_id = get_input("Enter the employee's department ID: ")

    department = Department.find_by_id(department_id)
    if department:
        create_entity(Employee, name=name, job_title=job_title, department_id=department_id)
    else:
        print("Error creating employee: department ID does not exist")


def update_employee():
    employee_id = get_input("Enter the employee's id: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        employee.name = get_input("Enter the employee's new name: ")
        employee.job_title = get_input("Enter the employee's new job title: ")
        employee.department_id = get_input("Enter the employee's new department ID: ")
        update_entity(employee)
    else:
        print(f'Employee {employee_id} not found')


def delete_employee():
    employee_id = get_input("Enter the employee's id: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        delete_entity(employee)
    else:
        print(f'Employee {employee_id} not found')


def list_department_employees():
    department_id = get_input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        list_entities(department.employees())
    else:
        print(f'Department {department_id} not found')


if __name__ == "__main__":
    options = {
        "1": list_departments,
        "2": find_department_by_name,
        "3": find_department_by_id,
        "4": create_department,
        "5": update_department,
        "6": delete_department,
        "7": list_employees,
        "8": find_employee_by_name,
        "9": find_employee_by_id,
        "10": create_employee,
        "11": update_employee,
        "12": delete_employee,
        "13": list_department_employees,
        "14": exit_program,
    }

    while True:
        print("\nPlease select an option:")
        print("1. List departments")
        print("2. Find department by name")
        print("3. Find department by ID")
        print("4. Create department")
        print("5. Update department")
        print("6. Delete department")
        print("7. List employees")
        print("8. Find employee by name")
        print("9. Find employee by ID")
        print("10. Create employee")
        print("11. Update employee")
        print("12. Delete employee")
        print("13. List department employees")
        print("14. Exit")

        option = input("Enter your choice: ")

        if option in options:
            options[option]()
        else:
            print("Invalid option. Please try again.")
