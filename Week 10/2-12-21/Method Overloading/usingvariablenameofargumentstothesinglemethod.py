class MethodOverloading: 
 def add(self,*args): 
  total=0 
  for i in args: 
   total+=i 
  return total 
 
s1=MethodOverloading() 
s1.add() 
print(s1.add(10)) 
print(s1.add(10,20)) 
print(s1.add(10,20,30)) 
print(s1.add(10,20,30,40)) 
print(s1.add(10,20,30,40,50,60,70))