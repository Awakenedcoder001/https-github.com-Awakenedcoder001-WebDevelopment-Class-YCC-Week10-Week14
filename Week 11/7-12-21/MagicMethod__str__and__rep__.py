class Student_Details: 
 def __init__(self,name,age,gender,did,course): 
  self.name=name 
  self.age=age 
  self.gender=gender 
  self.did=did 
  self.course=course 
 
 def __repr__(self): 
  print("Inside repr method") 
  return (f"Name Of te Student is : {self.name}\nAge of the Student is : {self.age}\nGender of the Student is :{self.gender}\nDID of the Student is : {self.did}\n Couse of the student is : {self.course}") 
 
 def __str__(self): 
  print("Inside str method") 
  return (f"Name Of te Student is : {self.name}\nAge of the Student is : {self.age}\nGender of the Student is :{self.gender}\nDID of the Student is : {self.did}\n Couse of the student is : {self.course}") 
 
obj=Student_Details(name="Pemba",age=10,gender="Shemale",did=420,course="Ex-Monk") 
print(obj)