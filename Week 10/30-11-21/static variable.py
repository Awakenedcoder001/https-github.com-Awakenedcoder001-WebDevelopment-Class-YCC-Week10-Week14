class WebDevelopment:
    course="Web Development"
    def __init__(self,name,age,gender):
        self.stu_name=name
        self.stu_age=age
        self.gender=gender

    def display(self):
        print(f"The name of the student is : {self.stu_name}")
        print(f"The age of the student is : {self.stu_age}")
        print(f"THe gender of the student is : {self.gender}")
        print(f"The course taken is : {self.course}")

s1=WebDevelopment(name="Tandin", age= 26, gender="Male")
s2=WebDevelopment(name="Tenzin", age=25, gender="Female")

print(WebDevelopment.__dict__)

print(s1.__dict__)
print(s2.__dict__)