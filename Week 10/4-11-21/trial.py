class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Employee(Person):
    def __init__(self,empid):
        #Constructor chain
        super().__init__
        self.empid=empid
    
    def display(self):
        print(f"Name of Employee is : {self.name}")
        print(f"Age of Employee is : {self.age}")
        print(f"Gender of Employee is : {self.gender}")
        print(f"Employee id is : {self.empid}")

obj=Employee()
obj.display