class Employees:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = int(age)
        self.salary = float(salary)

    def __str__(self):
        return f'Pracownik: {self.firstName} {self.lastName}, Wiek: {self.age}, Wynagrodzenie: {self.salary}'

    def __repr__(self):
        return self.__str__()
