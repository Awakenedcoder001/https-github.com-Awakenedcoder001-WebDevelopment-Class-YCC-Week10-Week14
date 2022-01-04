 """docstring for ClassName""" 
 def __init__(self,name,age,gender): 
  self.emp_name=name 
  self.emp_age=age 
  self.emp_gender=gender 
 
 def display(self): 
  #Deleting the variable inside the method 
  del self.emp_name 
 
emp_obj1=EmployeeDetails(name="Pemba",age=30,gender="Male") 
print(emp_obj1.__dict__) 
 
emp_obj1.display() 
#Deleting the variable outside the class 
print(emp_obj1.__dict__) 
 
del emp_obj1.emp_age 
print(emp_obj1.__dict__) 
 
emp_obj2=EmployeeDetails(name="Zangpo",age=90,gender="Male") 
print(emp_obj2.__dict__) 
 
emp_obj2.display() 
print(emp_obj2.__dict__)