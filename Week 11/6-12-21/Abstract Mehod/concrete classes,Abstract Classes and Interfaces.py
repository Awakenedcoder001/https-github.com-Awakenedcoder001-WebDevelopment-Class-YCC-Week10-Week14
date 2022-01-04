import abc 
class Students(abc.ABC): 
 @abc.abstractmethod 
 def details(self): 
  pass 
 
 @abc.abstractmethod 
 def name(self): 
  pass 
 
class WebDevelopment(Students): 
 def name(self): 
  self.stu_name=input("Enter the Strudents Name :") 
  print(f"Name of the student is : {self.stu_name}") 
 
class Details(WebDevelopment): 
 def details(self): 
  print(f"{self.stu_name} is a student of Web Development") 
 
obj1=Details() 
obj1.name() 
obj1.details()