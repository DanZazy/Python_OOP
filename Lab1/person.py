class Person:

    def __init__(self, name, surnm, mark = 1):
        self.name = name
        self.surnm = surnm
        self.mark = mark

    
    def low_grade(self):
        if self.mark > 85:
            print("Цей студент отримує стипендію")
        else:
            print("Цей студент НЕ ОТРИМУЄ СТИПЕНДІЮ")


    def get_info(self):
            print(f"Студент: {self.surnm}, {self.name}; Оцінка: {self.mark}")
    