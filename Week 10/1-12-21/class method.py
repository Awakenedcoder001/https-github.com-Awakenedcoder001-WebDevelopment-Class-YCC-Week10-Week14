class StudentDetails:
    course="Culinary Arts"
    def __init__(self):
        self.name=input("Enter your name : ")
        self.age=int(input("Enter your Age : "))
        self.average=float(input("Enter your average marks : "))

    def display(self):
        print(f"The name of the user is : {self.name}")
        print(f"The users age is : {self.age}")
        print(f"The marks the user has obtained is : {self.average}")

    @classmethod
    def class_method(cls):
        #Accessing the instance variables
        #print(f"Average is : {self.average}")
        
        #Note that
        
        #Accessing the satic variable inside class method
        print(f"The course the user has opted for is : {self.course}")

        #Accessing the static variable using cls variable
        print(f"Course is : {cls.course}")


students = StudentDetails()
students.display()
