def outer_function(func): 
 print("Inside Outer Function") 
 print(func) 
 
@outer_function 
def wish(): 
 print("Inside wish Function")