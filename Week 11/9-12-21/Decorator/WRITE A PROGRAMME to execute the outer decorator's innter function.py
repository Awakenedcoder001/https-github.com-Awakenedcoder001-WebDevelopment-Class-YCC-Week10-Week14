def deco1_outer_function(func): #2(adrees of greetings) 
 print("Inside Deco1 Outer Function") #3 
 print(func) #4 
 
 def deco1_inner_function(): 
  print("Inside Deco1 inner Function") 
 return deco1_inner_function #5 
 
 
def deco2_outer_function(func): #8 #Adress of deco1 inner function 
 print("Inside Deco2 Outer Function") #9 
 print(func) #10 
 
 def deco2_inner_function(): #15 
  print("Inside Deco2 inner Function") #16 
 return deco2_inner_function #11 
 
@deco2_outer_function #7 #12 #14 #17(Address of deco2 inner function) 
@deco1_outer_function #1 #6(Adress of deco1 inner function) 
def greeting(): 
 pass 
greeting() #13