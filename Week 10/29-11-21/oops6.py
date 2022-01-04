class DoctorLoday(object): 
 """docstring for ClassName""" 
 def __init__(self,name,age,gender): 
  self.name=name 
  self.age=age 
  self.gender=gender 
 
 def modify(self): 
  #Changing the instance variables inside the method 
  self.gender="Male" 
 
obj1=DoctorLoday(name="Loday",age=52,gender="Female") 
print(obj1.__dict__) 
 
obj1.modify() 
print(obj1.__dict__) 
 
#Changing the Instance Variables Outside the class 
obj1.age=60 
print(obj1.__dict__)

#{'name': 'Loday', 'age': 52, 'gender': 'Female'} 
{'name': 'Loday', 'age': 52, 'gender': 'Male'} 
{'name': 'Loday', 'age': 60, 'gender': 'Male'}