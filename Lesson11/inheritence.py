"""
Here is a sample people class. We can use it
as the parent class in our inheritance example.
"""
class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        print('My name is ' + self.name)


"""
Here is a Student class. While it captures important
information about being a student, a student is more
than just a grade and graduation year. In fact,
everything that the People class has is relevant to
the Student class. Luckily, we can inherit all of 
the methods and attributes from the Student class
"""
class Student: # update the class description to inherit from the People class
    def __init__(self, grade, grad_year): # update the __init__ params to include the People class's params
        # pass the params to the super function
        self.grade = grade
        self.grad_year = grad_year