class WebDevelpoment: 
 course="Web Developement" 
 def __init__(self,name,age,gender): 
  self.stu_name=name 
  self.stu_age=age 
  self.gender=gender 
 
 def display(self): 
  print(f"THE NAME OF THE STUDENT IS : {self.stu_name}") 
  print(f"THE AGE OF THE STUDENT IS : {self.stu_age}") 
  print(f"THE GENDER OF THE STUDENT IS : {self.gender}") 
  print(f"THE COURSE OF THE STUDENT IS : {self.course}") 
 
#Creating a Constructor 
s1=WebDevelpoment(name="Pemba",age=69,gender="Male") 
s2=WebDevelpoment(name="Tenzin",age=27.6,gender="Female") 
 
#Fetch the static variables : 
#classname.__dict__ 
print(WebDevelpoment.__dict__) 
 
#Fetching the instance Variables: 
print(s1.__dict__) 
print(s2.__dict__)