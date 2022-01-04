def Outer_Function(): 
 print("Outside outer function") 
 
 def inner_function(): 
  print("Inside inner function") 
 return inner_function 
 
fuc1=Outer_Function() 
print("Executed only outer function") 
fuc1() 
print(fuc1)