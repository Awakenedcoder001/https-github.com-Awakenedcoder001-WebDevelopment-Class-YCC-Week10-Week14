def Outer_Function(func): #2 
 print("Inside the Outer_Function") #3 
 print(func) #4 (Adress of divi) 
 
 def division(operand1,operand2): #9 
  print("Inside Divsion Function") #10 
  if operand2!=0: #11 
   func(operand1,operand2) #12 #16 
   print("Back To Division Operation") #17 
 
  else: 
   print("We can not divide by 0") 
 
 return division #5 
 
 
@Outer_Function #1 #6 #8 #18(Address of inner function) 
def divi(operand1,operand2): #13 
 result=operand1/operand2 #14 
 print(f"Result is :{result}") #15 
 
divi(operand1=20,operand2=0) #7 #19