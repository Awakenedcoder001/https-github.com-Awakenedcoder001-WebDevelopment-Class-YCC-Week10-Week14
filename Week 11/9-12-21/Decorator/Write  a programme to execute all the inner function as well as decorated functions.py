def deco1_outer_function(func): #2 
 print("Inside Deco1 Outer Function") #3  
 print(func) #4  
 
 def deco1_inner_function(): #18 
  print("Inside Deco1 inner Function")  #19 
  func() #20 #23 
  print("Control is back to deco1 inner function") #24 
 return deco1_inner_function #5 
 
def deco2_outer_function(func): #8 
 print("Inside Deco2 Outer Function") #9 
 print(func) #10 
 
 def deco2_inner_function(): #15  
  print("Inside Deco2 inner Function") #16 
  func() #17 #25 
  print("Control is back inside deco2 ineer function") #26 
 return deco2_inner_function #11 
 
@deco2_outer_function #7 #12 #14 #27 
@deco1_outer_function #1 #6 #28 
def greeting(): #21 
 print("Inside Greertings Function") #22 
greeting() #13