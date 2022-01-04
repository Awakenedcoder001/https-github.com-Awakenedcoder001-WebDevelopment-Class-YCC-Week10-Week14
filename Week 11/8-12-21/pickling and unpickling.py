import pickle
class StudentDetails:
 def __init__(self,name,gender,age,course):
  self.name=name
  self.age=age
  self.course=course
  self.gender=gender

name=input("Enter the student Name: ")
age=int(input("Enter the Students Age : "))
course=input("Enter the Course : ")
gender=input("Enter the Gender : ")


obj1=StudentDetails(name=name,age=age,gender=gender,course=course)

with open(file="serialize.txt",mode="wb") as file_write:
 pickle.dump(obj1,file_write)
 print("State of an Object Is Stored into the file ")