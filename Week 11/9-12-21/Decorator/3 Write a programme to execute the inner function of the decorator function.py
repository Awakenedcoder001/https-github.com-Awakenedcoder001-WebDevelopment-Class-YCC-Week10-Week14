def outer_function(func): 
 print("Inside outer function") 
 print(func) 
 
 def inner_function(): 
  print("Inside inner function") 
 return inner_function 
 
@outer_function 
def greetings(): 
 pass 
 
greetings() 
print("Executed Succesfully")