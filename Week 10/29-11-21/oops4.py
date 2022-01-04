class EmployeeDetails(object): 
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
del emp_obj1.emp_age 
print(emp_obj1.__dict__)


#{'emp_name': 'Pemba', 'emp_age': 30, 'emp_gender': 'Male'} 
{'emp_gender': 'Male'}