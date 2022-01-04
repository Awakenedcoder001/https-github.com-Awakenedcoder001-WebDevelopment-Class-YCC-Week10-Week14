import pickle
class StudentDetails:
 def __init__(self,name,gender,age,course):
  self.name=name
  self.age=age
  self.course=course
  self.gender=gender

 #Using instance method:
 def display(self):
  print(f"Name of the student is : {self.name}")
  print(f"Age of the student is : {self.age}")
  print(f"Course of the student is : {self.course}")
  print(f"GENDER of the student is : {self.gender}")

 #Using str
 def __str__(self):
  return (f"Name Of te Student is : {self.name}\nAge of the Student is : {self.age}\nGender of the Student is :{self.gender}\nCouse of the student is : {self.course}")

name=input("Enter the student Name: ")
age=int(input("Enter the Students Age :"))
course=input("Enter the Course :")
gender=input("Enter the Gender :")

obj1=StudentDetails(name=name,age=age,gender=gender,course=course)

#Performing pickling operation
with open(file="serialize.txt",mode="wb") as file_write:
 pickle.dump(obj1,file_write)
 print("State of an Object Is Stored into the file ")

#Performing Unpickling operation
with open(file="serialize.txt",mode="rb") as file_read:
 #In the reference of obj2 the address of an object is stored
 obj2=pickle.load(file_read)
 print(obj2)

 #Calling the instance method using reference
 obj2.display()