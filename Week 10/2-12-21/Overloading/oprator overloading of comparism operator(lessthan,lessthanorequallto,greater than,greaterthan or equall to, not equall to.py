class Operator_overloading: 
 def __init__(self,num): 
  self.num=num 
 
 def __lt__(self,other): 
  print(f"{self.num} IS LESS THAN  {other.num} : {self.num < other.num}") 
  
 def __le__(self,other): 
  print(f"{self.num} IS LESS THAN OR EQUAL TO  {other.num} : {self.num <= other.num}") 
  
 def __gt__(self,other): 
  print(f"{self.num} IS GREATER THAN  {other.num} : {self.num > other.num}") 
  
 def __ge__(self,other): 
  print(f"{self.num} IS GREATER THAN OR EQUAL TO  {other.num} : {self.num >= other.num}") 
 
 def __eq__(self,other): 
  print(f"{self.num} IS EQUAL TO  {other.num} : {self.num == other.num}") 
  
 def __ne__(self,other): 
  print(f"{self.num} IS NOT EQUAL TO  {other.num} : {self.num != other.num}") 
  
  
 
s1=Operator_overloading(69) 
s2=Operator_overloading(98) 
s1<s2 
s1<=s2 
s1>s2 
s1>=s2 
s1==s2 
s1!=s2