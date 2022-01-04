class MethodOverloading: 
 def add(self,a,b): 
  sum=a+b 
  return sum 
 
 def add(self,a,b,c,d): 
  sum=a+b+c+d 
  return sum 
 
 def add(self,a,b,c): 
  sum=a+b+c 
  return sum 
 
s1=MethodOverloading() 
 
res=s1.add(a=10,b=20,c=30) 
print(res) 
 
#Error:TypeError 
res=s1.add(10,20) 
print(res)