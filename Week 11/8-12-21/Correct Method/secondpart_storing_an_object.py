import pickle
from firstpart_Creating_an_Object import Employee_Details
n=int(input("Enter the No Of Employees :"))
for i in range(n):
 eid=input("Enter the ID of the Employee :")
 name=input("Enter the Name of the Employee :")
 role=input("Enter the Role of the Employee :")
 age=int(input("Enter the Age of the Employee :"))
 bloodgroup=input("Enter the BloodGroup of the Employee :")
 gender=input("Enter the Gender of the Employee :")

 emp1=Employee_Details(eid=eid,name=name,role=role,bloodgroup=bloodgroup,age=age,gender=gender)

 with open(file="thazay_2.txt",mode="ab") as file_write:
  pickle.dump(emp1,file_write)

print("Data Is stored Inside the Object File")
