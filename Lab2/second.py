class Robot:

    def __init__(self, car, printer, lamp):
        self.car = car
        self.printer = printer
        self.lamp = lamp

    def do_it(self):
        self.printer.does()
        self.lamp.does()
        self.car.does()


class Printer:
    def does(self):
        print("Printer does print!")

class Lamp:
    def does(self):
        print("Lamp does glow!")

class Car:
    def does(self):
        print("Car does ride!")


#class SportResults:

#   points = 150

# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number

#     def dump(self):
#         print(self.name, self.symbol, self.number)

# from abc import ABC, abstractmethod

# class Country(ABC):

#     @abstractmethod
#     def currency(self):
#         pass

# class Switzerland(Country):
#     def currency(self):
#         print("The national currency for this country is franc")

# class England(Country):
#     def currency(self):
#         print("The national currency for this country is pound")
     

# class Japan(Country):
#     def currency(self):
#         print("The national currency for this country is yen")
    

# switzerland = Switzerland()
# england = England()
# japan = Japan()

# japan.currency()