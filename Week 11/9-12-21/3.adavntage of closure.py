def Outer_Function(name): #2 
 print("Inside Outer_Function") #3 
 print(f"Name of the Person is : {name}") #4 
  
 def inner_function(): #9 
  print("Inside inner function") #10 
  print(f"Name of the Person is  : {name}") #11 
 
 return inner_function #5 
 
func1=Outer_Function("Thazay") #1 #6 --> Address of the inner_function 
print(func1) #7 
 
func1() #8 #12 
del Outer_Function #13 --> deleted the outer function 
 
func1() #14 
 
Outer_Function() #15 #Error