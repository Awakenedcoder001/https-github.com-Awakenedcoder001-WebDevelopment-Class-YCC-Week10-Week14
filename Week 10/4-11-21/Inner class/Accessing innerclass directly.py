class OuterClass: 
 def o_method1(self): 
  print("Inside Outer Class Method") 
 
 class InnerClass: 
  def method1(self): 
   print("Inside Inner Class Method1") 
 
  def method2(self): 
   print("Inside Inner Class Method2") 
 
ref=OuterClass() 
ref.o_method1() 
 
#Craete an object of Inner class: 
#Create an object of outer class 
ref1=OuterClass().InnerClass() 
ref1.method1() 
ref1.method2() 
 
#Using the outer class Object Refernce 
ref2=ref.InnerClass() 
ref2.method1() 
ref2.method2() 
 
#Accessing Innerclass directly  
ref3=InnerClass() #NameError : name InnerClass is not defined