class StudentDetails: 
 course="Web Development" 
 def __init__(self): 
  self.name=input("Enter the name : ") 
  self.age=int(input("Enter the age : ")) 
  self.average=float(input("Enter the average : ")) 
  
 def display(self): 
  print(f"Name is :{self.name}") 
  print(f"Age is :{self.age}") 
  print(f"Average is :{self.average}") 
  
 @classmethod 
 def class_method(cls): 
  #Accessing the static variable inside class method 
  print(f"course is :{StudentDetails.course}") 
 
  #Accessing The static variable using cls variable 
  print(f"course is :{cls.course}") 
 
 
obj1=StudentDetails() 
obj1.display() 
 
#objrefernce 
obj1.class_method()