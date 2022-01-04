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