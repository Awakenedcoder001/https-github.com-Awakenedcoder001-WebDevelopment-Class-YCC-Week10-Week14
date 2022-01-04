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
        print(f"The course the user has opted for is : {self.course}")


students = StudentDetails()
students.display()
