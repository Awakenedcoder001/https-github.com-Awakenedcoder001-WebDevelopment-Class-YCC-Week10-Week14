class Operator_overloading: 
 def __init__(self,name,num): 
  self.name=name 
  self.num=num 
 
s1=Operator_overloading("Tandin",69) 
s2=Operator_overloading("Tshewang",98) 
# Error:TypeError(Cannot add the object references) 
s1+s2