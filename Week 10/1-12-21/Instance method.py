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
  #Accessing the static variable inside instance method 
  print(f"course is :{StudentDetails.course}") 
 
obj1=StudentDetails() 
obj1.display()


#Enter the name : pemba 
#Enter the age : 88 
#Enter the average : 10.2 
#Name is :pemba 
#Age is :88 
#Average is :10.2 
#course is :Web Development