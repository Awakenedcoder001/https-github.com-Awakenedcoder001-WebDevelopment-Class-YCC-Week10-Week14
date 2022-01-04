class SettersGetters:
    def set_empname(self,name):
        self.empname=name

    def set_empage(self,age):
        self.empage=age

    def get_empname(self):
        return self.empname
    
    def get_empage(self):
        return self.empage

s1=SettersGetters()
name=input("Enter you name : ")
age=int(input("enter the age : "))

s1.set_empname(name=name)
s1.set_empage(age=age)

emp_name=s1.get_empname()
print(f"The name of the employee is : {emp_name}")

emp_age=s1.get_empage()
print(f"The age of the employee is : {emp_age}")

