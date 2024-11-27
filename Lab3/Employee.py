class Employees:
    def __init__(self, firstName,lastName,age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def getInfo(self):
        return (f"Imię: {self.firstName}"
                f"Nazwisko: {self.lastName} \t"
                f"Wiek: {self.age} \t "
                f"Wynagrodzenie: {self.salary}")

    def __str__(self): #to jest string
        return (f'Pracownik: {self.firstName} {self.lastName} \t'
                f'Wiek: {self.age} \t'
                f'Wynagrodzenie: {self.salary}')

    def __repr__(self): #to jest obiekt
        return (f'Pracownik: {self.firstName} {self.lastName} \t'
                f'Wiek: {self.age} \t'
                f'Wynagrodzenie: {self.salary}')
