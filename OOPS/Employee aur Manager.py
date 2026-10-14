
from abc import ABC, abstractmethod


# 1. Abstraction
class Employee(ABC):

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id       # Public
        self.name = name                     # Public
        self._department = department        # Protected
        self.__salary = salary               # Private

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = amount

    @abstractmethod
    def display_details(self):
        pass

    def update_salary(self, amount, bonus=0):
        """Default arguments demonstrate flexible method behavior."""
        if amount < 0 or bonus < 0:
            raise ValueError("Salary and bonus cannot be negative.")

        self.salary = amount + bonus

    def update_department(self, department):
        self._department = department


# 2. Inheritance
class Manager(Employee):

    def __init__(
        self, employee_id, name, salary, department, team_size
    ):
        super().__init__(employee_id, name, salary, department)
        self.team_size = team_size

    # 3. Method overriding
    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Role: Manager")
        print(f"Department: {self._department}")
        print(f"Salary: Rs. {self.salary:,.2f}")
        print(f"Team Size: {self.team_size}")


class Developer(Employee):

    def __init__(
        self, employee_id, name, salary, department, programming_language
    ):
        super().__init__(employee_id, name, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Role: Developer")
        print(f"Department: {self._department}")
        print(f"Salary: Rs. {self.salary:,.2f}")
        print(f"Programming Language: {self.programming_language}")


# 4. Employee Management System
class EmployeeManagementSystem:

    def __init__(self):
        self.__employees = {}

    def add_employee(self, employee):
        if employee.employee_id in self.__employees:
            print("Error: Employee ID already exists.")
            return

        self.__employees[employee.employee_id] = employee
        print("Employee added successfully.")

    def view_employees(self):
        if not self.__employees:
            print("No employees found.")
            return

        for employee in self.__employees.values():
            employee.display_details()

    def search_employee(self, employee_id):
        employee = self.__employees.get(employee_id)

        if employee:
            employee.display_details()
        else:
            print("Employee not found.")

    def update_salary(self, employee_id):
        employee = self.__employees.get(employee_id)

        if not employee:
            print("Employee not found.")
            return

        try:
            amount = float(input("Enter new base salary: "))
            bonus = float(input("Enter bonus (0 if none): "))

            employee.update_salary(amount, bonus)
            print("Salary updated successfully.")

        except ValueError as error:
            print(f"Invalid input: {error}")

    def update_department(self, employee_id):
        employee = self.__employees.get(employee_id)

        if not employee:
            print("Employee not found.")
            return

        department = input("Enter new department: ").strip()

        if not department:
            print("Department cannot be empty.")
            return

        employee.update_department(department)
        print("Department updated successfully.")

    def delete_employee(self, employee_id):
        if employee_id in self.__employees:
            del self.__employees[employee_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def run(self):
        while True:
            print("EMPLOYEE MANAGEMENT SYSTEM ")
            print("1. Add Manager")
            print("2. Add Developer")
            print("3. View All Employees")
            print("4. Search Employee")
            print("5. Update Salary")
            print("6. Update Department")
            print("7. Delete Employee")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    employee_id = input("Employee ID: ").strip()
                    name = input("Name: ").strip()
                    salary = float(input("Salary: "))
                    department = input("Department: ").strip()
                    team_size = int(input("Team size: "))

                    if not employee_id or not name or not department:
                        print("ID, name and department are required.")
                        continue

                    if salary < 0 or team_size < 0:
                        print("Salary and team size cannot be negative.")
                        continue

                    manager = Manager(
                        employee_id, name, salary, department, team_size
                    )
                    self.add_employee(manager)

                elif choice == "2":
                    employee_id = input("Employee ID: ").strip()
                    name = input("Name: ").strip()
                    salary = float(input("Salary: "))
                    department = input("Department: ").strip()
                    language = input("Programming language: ").strip()

                    if not employee_id or not name or not department or not language:
                        print("All fields are required.")
                        continue

                    if salary < 0:
                        print("Salary cannot be negative.")
                        continue

                    developer = Developer(
                        employee_id, name, salary, department, language
                    )
                    self.add_employee(developer)

                elif choice == "3":
                    self.view_employees()

                elif choice == "4":
                    employee_id = input("Enter Employee ID: ").strip()
                    self.search_employee(employee_id)

                elif choice == "5":
                    employee_id = input("Enter Employee ID: ").strip()
                    self.update_salary(employee_id)

                elif choice == "6":
                    employee_id = input("Enter Employee ID: ").strip()
                    self.update_department(employee_id)

                elif choice == "7":
                    employee_id = input("Enter Employee ID: ").strip()
                    self.delete_employee(employee_id)

                elif choice == "8":
                    print("Exiting Employee Management System.")
                    break

                else:
                    print("Invalid choice. Please try again.")

            except (ValueError, TypeError) as error:
                print(f"Invalid input: {error}")


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.run()
