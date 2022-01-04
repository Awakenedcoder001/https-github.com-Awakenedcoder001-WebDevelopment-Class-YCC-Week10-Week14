#Constructor Overloading: 
#1. Python does not support Constructor overloading 
#2. If we define multiple constructor then the last 
#   constructor present in the constructor hierachy 
# would be taken into consideration 
 
 
class Constructor: 
 def __init__(self): 
  print("With Zero No Of Arguements") 
 
 def __init__(self,a): 
  return a 
 
 def __init__(self,a,b): 
  print(a+b)  
 
c=Constructor(10,20) 
print(c) 
 
#TypeError: Constructor.__init__() missing 2 required positional arguments: 'a' and 'b' 
c=Constructor() 
print(c)