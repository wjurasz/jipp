#from abc import ABC, abstractmethod
# class Pojazd(ABC):
#     @abstractmethod
#     def info(self):
#         pass

class Pojazd():
    def __init__(self, typ):
        self.type = typ

class  Samochod(Pojazd):
    def __init__(self,marka, model, rok):
        super().typ
        self.__marka = marka #priviet to __ przy self
        self.model = model
        self.rok = rok

    def opis(self):
        return f"{super.typ, self.marka} {self.model} {self.rok}"

samochod1 = Samochod("toyota", "corolla", 2005)
print(samochod1.opis())