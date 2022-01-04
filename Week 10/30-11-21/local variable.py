class WebDevelpoment: 
 def __init__(self,name,age,gender,course): 
  self.stu_name=name 
  self.stu_age=age 
  self.gender=gender 
  self.course=course 
 
 def display(self): 
  print(f"THE NAME OF THE STUDENT IS : {self.stu_name}") 
  print(f"THE AGE OF THE STUDENT IS : {self.stu_age}") 
  print(f"THE GENDER OF THE STUDENT IS : {self.gender}") 
  print(f"THE COURSE OF THE STUDENT IS : {self.course}") 
 
#Creating a Constructor 
s1=WebDevelpoment(name="Pemba",age=69,gender="Male",course="webdevelopment") 
s2=WebDevelpoment(name="Tenzin",age=27.6,gender="Female",course="webdevelopment") 
s1.display() 
s2.display()