class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        married = "Married" if self.is_married else "Not married"
        print(f'Full name: {self.full_name}, Age: {self.age}, {married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_marks(self):
        return round(sum(self.marks.values()) / len(self.marks), 1)


class Teacher(Person):
    base_salary = 20000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def bonus_to_salary(self):
        salary = self.base_salary
        if self.experience > 3:
            print(f'Experience: {self.experience}')
            for year in range(4, self.experience + 1):
                salary += salary * 0.05
        else:
            print("Teacher's experience is too low")

        return round(salary, 2)


teacher = Teacher("Azamat Kudzaev", 33, True, 5)
teacher.introduce_myself()
print(f"Salary: {teacher.bonus_to_salary()}")


def create_students():
    students = []
    students.append(Student("Beishebaev Argen", 20, False, {"Math": 5, "English": 4, "Russian": 5, "Chemistry": 3}))
    students.append(Student("Taalaev Emir", 19, False, {"English": 5, "Russian": 5}))
    students.append(Student("Tagaibekova Astra", 20, False, {"Math": 5, "English": 5, "Chemistry": 5}))
    return students


students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(f"Предмет: {subject}, оценка: {mark}")
    print(f'Средняя оценка: {student.average_marks()}')
