class MethodOverloading: 
 def add(self,a=None,b=None,c=None,d=None): 
  if a!=None and b!=None and c!=None and d!=None: 
   res=a+b+c+d 
   return res 
 
  elif a!=None and b!=None and c!=None: 
   res=a+b+c 
   return res 
 
  elif a!=None and b!=None: 
   res=a+b 
   return res 
 
  elif a!=None: 
   return a 
 
  else: 
   print("No arguemnts is passed") 
 
s1=MethodOverloading() 
s1.add() 
print(s1.add(10)) 
print(s1.add(10,20)) 
print(s1.add(10,20,30)) 
print(s1.add(10,20,30,40))