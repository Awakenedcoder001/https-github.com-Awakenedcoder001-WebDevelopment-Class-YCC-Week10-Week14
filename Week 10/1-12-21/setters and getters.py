class SettersGetters: 
 def set_empname(self,name): 
  self.empname=name 
 
 def set_empage(self,age): 
  self.age=age 
 
 def get_empname(self): 
  return self.empname 
 
 def get_empage(self): 
  return self.age 
 
s1=SettersGetters() 
name=input("ENTER THE NAME :") 
age=int(input("ENTER THE AGE :")) 
 
s1.set_empname(name=name) 
s1.set_empage(age=age) 
emp_name=s1.get_empname() 
print(f"THE NAME OF TEH EMPLOYEE IS : {emp_name}") 
 
emp_age=s1.get_empage() 
print(f"THE AGE OF THE EMPLOYEE IS : {emp_age}")