from person import Person

student_count = int(input("Введіть кількість студентів: "))

students = []

i = 1

while i <= student_count:
    istr = str(i)
    name = input("Введіть ім'я студента № : "+ istr)
    surname = input("Введіть прізвище студента № : "+istr)
    mark = int(input("Введіть оцінку студента № : " +istr))
    person = Person(name,surname,mark)
    i += 1
    students.append(person)

for student in students:
    student.get_info()
    student.low_grade()


