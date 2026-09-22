from second import Robot
from second import Car
from second import Printer
from second import Lamp

car1 = Car()
printer1 = Printer()
lamp1 = Lamp()

robot1 = Robot(printer=printer1, car=car1, lamp=lamp1)

robot1.do_it()

# from second import Element

# argentum = Element('Argentum', 'Ag', 47)

# argentum.dump()

# e1 = Element("Silicium", "Si", 14)

# print(e1.name)
# print(e1.symbol)
# print(e1.number)

# elements = ['Argentum', 'Ag', 47]

# argentum = Element(elements[0], elements[1], elements[2])

# print(argentum.name)
# print(argentum.symbol)
# print(argentum.number)


# diving = SportResults()

# print(diving.points)


