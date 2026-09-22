class Person:

    def __init__(self, name, surnm, mark =1):
        self.name = name
        self.surnm = surnm
        self.mark = mark

    def grade(self):
        print(f"Студент: {self.surnm}, {self.name}; Оцінка: {self.mark}")

    def __del__(self):
        print(f"Студент {self.surnm} {self.name} отримує стипендію!")