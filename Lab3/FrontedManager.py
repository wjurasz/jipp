from Manager import *
from Utility import inputValue

class FrontedManager:
    def __init__(self):
        self.Manager = Manager()

    def print_menu(self):
        print("\n🔹 Zarządzanie pracownikami 🔹\n")
        message = [
            '1. Dodaj pracownika',
            '2. Wyświetl pracowników',
            '3. Usuń pracownika',
            '4. Aktualizacja wynagrodzeń',
            '5. Wyjście'
        ]
        print('\n'.join(message))
        return inputValue("Wybierz opcję (1-5): ", 1, 5)

    def run(self):
        if not self.Manager.login():
            return

        while True:
            choice = self.print_menu()
            if choice == 1:
                self.Manager.add_Employee()
            elif choice == 2:
                self.Manager.view_employees()
            elif choice == 3:
                self.Manager.remove_Employee()
            elif choice == 4:
                firstName = input("Podaj imię: ").strip()
                lastName = input("Podaj nazwisko: ").strip()
                salary = input("Podaj nowe wynagrodzenie: ").strip()
                self.Manager.update_employees(firstName, lastName, salary)
            elif choice == 5:
                print("Wylogowano.")
                break
