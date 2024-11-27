from Employee import *
class Manager:
    def __init__(self):
        self.employees = []

    def add_Employee(self):
        print("Podaj dane pracownika: ")
        firstName = input('Podaj imie')
        lastName = input('Podaj nazwisko')
        age = input("Podaj wiek")
        salary = input("Podaj wynagrodzenie")
        self.employees.append(Employees(firstName, lastName, age, salary))

    def view_employees(self):
        if len(self.employees) == 0:
            print("\n Brak pracowników w bazie")
            return
        else:
            for emp in self.employees:
                print(emp)

    def deleteEmployee(self,age_from, age_to):
        for emp in self.employees:
            if age_from <= emp.age <= age_to:
                print(f'\tUsunięto pracownika: {emp.name}')
                self.employees.remove(emp)

    def find_Employee(self, firstName, lastName):
        for emp in self.employees:
            if emp.firstName == firstName and emp.lastName == lastName:
                return emp
            return None

    def update_employee_salary(self, firstName, lastName, salary):
        emp = self.find_Employee(firstName, lastName)
        if emp is None:
            print("Nie znaleziono pracownika")
            return
        else:
            emp.salary = salary
            print(f'Wynagrodzenie pracownika zmienione na: {emp.salary}')
            return




