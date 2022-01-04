import pickle
class StudentDetails:
    def __init__(self,name,gender,age,course):
        self.name = name
        self.gender = gender
        self.age = age
        self.course = course
    
Sname=input("Enter the std NAME : ")
Sage=int(input("Enter the std AGE : "))
Scourse=input("Enter the COURSE the STD is taking : ")
Sgender=input("Enter the GENDER of the student : ")

sinfo=StudentDetails(name=Sname,age=Sage, gender=Sgender, course=Scourse)

with open(file="newstudentinfo.txt", mode="wb") as file_write:
    pickle.dump(sinfo,file_write)
    print("Object has been printed")
