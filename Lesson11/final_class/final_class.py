class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        print('My name is ' + self.name)


class Student(People):
    def __init__(self, name, age, gender, grade, gradYear):
        super( ).__init__(name, age, gender)
        self.grade = grade
        self.gradYear = gradYear

    def graduate(self):
        print('I am in ' + self.grade + ' grade and I will graduate in ' + self.gradYear)
        

newStudent = Student('Letty', 16, 'Female', '11th', '2023')
newStudent.graduate()
print(newStudent.gender)
newStudent.talk()