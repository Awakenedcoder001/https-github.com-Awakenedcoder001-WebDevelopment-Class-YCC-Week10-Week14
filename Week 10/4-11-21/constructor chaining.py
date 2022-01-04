class Person: 
 def __init__(self,name,age,gender): 
  self.name=name 
  self.age=age 
  self.gender=gender 
class Employee(Person): 
 def __init__(self,empid): 
  name=input("ENTER THE NAME :") 
  age=int(input("ENTER THE AGE :")) 
  gender=input("ENTER THE GENDER :") 
  super().__init__(name=name,age=age,gender=gender) 
  self.empid=empid 
 
 def display(self): 
  print(f"Name of the Employee is :{self.name}") 
  print(f"Age of the Employee is:{self.age}") 
  print(f"Gender of the Employee is:{self.gender}") 
  print(f"Empid of the Employee is:{self.empid}") 
 
obj=Employee(1001) 
obj.display()