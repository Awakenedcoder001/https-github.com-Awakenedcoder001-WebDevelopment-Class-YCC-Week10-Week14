import pickle
class Employee_Details:
 def __init__(self,eid,name,role,age,bloodgroup,gender):
  self.eid=eid
  self.name=name
  self.role=role
  self.age=age
  self.bloodgroup=bloodgroup
  self.gender=gender

 def display(self):
  print(f"Employee ID  IS : {self.eid}")
  print(f"Employee Name is : {self.name}")
  print(f"Employee Role is : {self.role}")
  print(f"Employee Age is : {self.age}")
  print(f"Employee BloodGroup is : {self.bloodgroup}")
  print(f"Employee Gender is: {self.gender}")


n=int(input("Enter the No Of Employees :"))
for i in range(n):
 eid=input("Enter the ID of the Employee :")
 name=input("Enter the Name of the Employee :")
 role=input("Enter the Role of the Employee :")
 age=int(input("Enter the Age of the Employee :"))
 bloodgroup=input("Enter the BloodGroup of the Employee :")
 gender=input("Enter the Gender of the Employee :")

 emp1=Employee_Details(eid=eid,name=name,role=role,bloodgroup=bloodgroup,age=age,gender=gender)

 with open(file="thazay_1.txt",mode="ab") as file_write:
  pickle.dump(emp1,file_write)

print("Data Is stored Inside the Object File")


file_read=open(file="thazay_1.txt",mode='rb')
while True:
 try:
  employee_details=pickle.load(file_read)
  employee_details.display()

 except EOFError as msg:
  break;

 except Exception as msg:
  break;