class WebDevelopment:
    def __init__(self,name,age,gender,course):
        self.stu_name=name
        self.stu_age=age
        self.gender=gender
        self.course=course
    def display(self):
        print(f"The name of the student is: {self.stu_name}")
        print(f"The age of the student is : {self.stu_age}")
        print(f"The gender of the student is : {self.gender}")
        print(f"The Course the student is taking is : {self.course}")

#creating a constructor function
s1=WebDevelopment(name="Chormalik", age="40", gender="Male",course="Webdevelopment")
s2=WebDevelopment(name="Sonam",age=40,gender="Male",course="BBA")
s3=WebDevelopment(name="Tenzin",age=22,gender="Female",course="BCA")
s4=WebDevelopment(name="Thinleay",age=30,gender="Female",course="LLB")
s1.display()
s2.display()