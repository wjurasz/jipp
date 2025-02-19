import json
from Employee import Employees

class Manager:
    def __init__(self):
        self.employees = []
        self.load_data()

    def save_data(self):
        with open("employees.json", "w") as file:
            json.dump([emp.__dict__ for emp in self.employees], file, indent=4)

    def load_data(self):
        try:
            with open("employees.json", "r") as file:
                data = json.load(file)
                self.employees = [Employees(**emp) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []

    def login(self):
        username = input("Podaj login: ")
        password = input("Podaj hasło: ")
        if username == "admin" and password == "admin":
            print("Zalogowano pomyślnie!\n")
            return True
        else:
            print("Błędny login lub hasło!\n")
            return False

    def add_Employee(self):
        print("Podaj dane pracownika: ")
        firstName = input('Imię: ').strip()
        lastName = input('Nazwisko: ').strip()
        while True:
            try:
                age = int(input("Wiek: ").strip())
                salary = float(input("Wynagrodzenie: ").strip())
                break
            except ValueError:
                print("Nieprawidłowe dane. Wiek musi być liczbą całkowitą, a wynagrodzenie liczbą zmiennoprzecinkową.")

        self.employees.append(Employees(firstName, lastName, age, salary))
        self.save_data()
        print("Dodano pracownika!")

    def view_employees(self):
        if not self.employees:
            print("\nBrak pracowników w bazie")
        else:
            for emp in self.employees:
                print(emp)

    def remove_Employee(self):
        if not self.employees:
            print("\nBrak pracowników w bazie")
            return
        
        firstName = input("Podaj imię pracownika do usunięcia: ").strip()
        lastName = input("Podaj nazwisko: ").strip()
        found = False
        
        for emp in self.employees:
            if emp.firstName == firstName and emp.lastName == lastName:
                self.employees.remove(emp)
                found = True
                print(f"Usunięto pracownika: {firstName} {lastName}")
                break
        
        if not found:
            print("Nie znaleziono pracownika.")
        
        self.save_data()

    def update_employees(self, firstName, lastName, salary):
        emp = self.find_Employee(firstName, lastName)
        if emp is None:
            print("Nie znaleziono pracownika")
        else:
            emp.salary = salary
            print(f'Wynagrodzenie zmienione na: {emp.salary}')
            self.save_data()

    def find_Employee(self, firstName, lastName):
        for emp in self.employees:
            if emp.firstName == firstName and emp.lastName == lastName:
                return emp
        return None
