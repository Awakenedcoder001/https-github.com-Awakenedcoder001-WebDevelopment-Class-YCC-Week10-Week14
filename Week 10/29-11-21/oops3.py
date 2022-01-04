class EmployeeDetails(object): 
 """docstring for ClassName""" 
 def __init__(self,name,age): 
  self.emp_name=name 
  self.emp_age=age 
 
 
 def display(self,gender): 
  self.emp_gender=gender 
  #Accessing the varibles inside the class 
  print(f"AGE OF THE EMPLOYEE IS : {self.emp_age}") 
  print(f"NAME OF THE EMPLOYEE IS : {self.emp_name} ") 
 
emp_obj1=EmployeeDetails(name="Pemba",age=30) 
 
emp_obj1.display("Male") 
 
#Accessing the instance variable outside the class 
print(f"GENDER OF THE EMPLOYEE IS : {emp_obj1.emp_gender}")


#AGE OF THE EMPLOYEE IS : 30 
NAME OF THE EMPLOYEE IS : Pemba 
GENDER OF THE EMPLOYEE IS : Male