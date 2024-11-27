from Manager import *
from Employee import *
from Utility import inputValue
class FrontedManager:
    def __init__(self):
        self.Manager = Manager()


    def print_menu(self):
        print("\nZarzdzanie pracownikami\n")
        message = [
            '1. Dodaj pracownika',
            '2. Wyświetl pracowników',
            '3. Usuń pracownika ',
            '4. Aktualizacja wynagrodzeń',
            '5. Wyjście'
        ]
        print('\n'.join(message))
        msg = f"Wybierz opcje:  (1- {len(message)})"
        return inputValue(msg,1,len(message))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.Manager.add_Employee()
            elif choice == 2:

                self.Manager.view_employees()
            elif choice == 3:
                age_from = int(input("Podaj poczatek przedzialu wieku pracownika: "))
                age_to = int(input("Podaj koniec przedzialu wieku pracownika: "))
                self.Manager.remove_Employee()
            elif choice == 4:
                firstName = input("Podaj imie:  ")
                lastName = input("Podaj nazwisko:  ")
                salary = input("Podaj wynagrodzenie:  ")
                self.Manager.update_employees(firstName,lastName,salary)
            elif choice == 5:
                break
            else:
                print("Nie znaleziono opcji")
                continue
