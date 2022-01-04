class Operator_overloading: 
 def __init__(self,name,num): 
  self.name=name 
  self.num=num 
 
 def __add__(self,other): 
  print(f"Name is:{self.name+other.name}") 
  print(f"Average is:{(self.num+other.num)/2}") 
   
s1=Operator_overloading("Tandin",69) 
s2=Operator_overloading("Tshewang",98) 
s1+s2