class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

# Create a list of Employee objects
employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

def search_by_age(operator, age):
    result = []
    if operator == ">":
        result = [emp for emp in employees if emp.age > age]
    elif operator == "<":
        result = [emp for emp in employees if emp.age < age]
    elif operator == ">=":
        result = [emp for emp in employees if emp.age >= age]
    elif operator == "<=":
        result = [emp for emp in employees if emp.age <= age]
    return result

def search_by_salary(operator, salary):
    result = []
    if operator == ">":
        result = [emp for emp in employees if emp.salary > salary]
    elif operator == "<":
        result = [emp for emp in employees if emp.salary < salary]
    elif operator == ">=":
        result = [emp for emp in employees if emp.salary >= salary]
    elif operator == "<=":
        result = [emp for emp in employees if emp.salary <= salary]
    return result

def search_by_emp_id(emp_id):
    result = [emp for emp in employees if emp.emp_id == emp_id]
    return result

while True:
    print("Menu:")
    print("1. Search by Age")
    print("2. Search by Salary")
    print("3. Search by Employee ID")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        operator = input("Enter operator (>, <, <=, >=): ")
        age = int(input("Enter age: "))
        result = search_by_age(operator, age)
    elif choice == "2":
        operator = input("Enter operator (>, <, <=, >=): ")
        salary = int(input("Enter salary: "))
        result = search_by_salary(operator, salary)
    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        result = search_by_emp_id(emp_id)
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
        continue
    
    if not result:
        print("No matching records found.")
    else:
        print("Matching Records:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
