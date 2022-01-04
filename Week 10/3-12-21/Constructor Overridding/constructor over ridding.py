class Person: 
 def __init__(self,name,age,gender,weight): 
  self.name=name 
  self.age=age 
  self.gender=gender 
  self.weight=weight 
 
 def display(self): 
  print(f"NAME OF THE PERSON IS : {self.name}") 
  print(f"AGE OF THE PERSON IS : {self.age}") 
  print(f"GENDER OF THE PERSON IS : {self.gender}") 
  print(f"WEIGHT OF THE PERSON IS : {self.weight}") 
 
class Employee(Person): 
 pass 
 
emp_1=Employee(name="Pemba",age=30,gender="Male",weight=40) 
emp_1.display()