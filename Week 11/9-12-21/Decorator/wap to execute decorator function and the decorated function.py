def outer_function(func):#2 (address of greetings) 
 print("Inside outer function")#3 
 print(func)#4 
 
 def inner_function(name):#9 
  if name.lower()=='pemba':#10 
   func(name)#11 #14 
  else: 
   print("Get lost you Silicos") 
 return inner_function #5 
   
@outer_function #1 #6(address of the inner function)#8 
def greetings(name):#12 
 print(f"{name},how are you")#13 
greetings('pemba')#7 #15 
print("Executed Successfully")#16