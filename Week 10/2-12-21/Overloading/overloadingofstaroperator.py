class Operator_overloading: 
 def __init__(self,num): 
  self.num=num 
 
 def __mul__(self,other): 
  print(f"MULTIPLATICATION OF {self.num} * {other.num} IS : {self.num * other.num}") 
    
s1=Operator_overloading(69) 
s2=Operator_overloading(98) 
s1*s2 
 
s1=Operator_overloading("**") 
s2=Operator_overloading(2) 
s1*s2

