class Person:
    def __init__(self):
        self.name=input("enter the name")
        self.dob=self.DateOfBirth()

    def display(self):
        print(f"Name of the person is: {self.name}")
        self.dob.display()
    

class DateOfBirth:
    def __init__(self):
        self.date=int(input("Enter the date of birth"))
        self.month=int(input("Enter the Month number of birth"))
        self.year=int(input("Enter the year of birth"))

    def display(self):
        print(f"Date of birth is : {self.date}:{self.month}:{self.year}")

ref=Person()
ref.display



