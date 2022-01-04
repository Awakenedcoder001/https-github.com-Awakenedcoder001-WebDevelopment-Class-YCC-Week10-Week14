class WebDevelpoment: 
 course="Web Developement" 
 def __init__(self): 
  WebDevelpoment.gravity=9.8 
 
 def static_variable(self): 
  WebDevelpoment.programming="Python" 
   
#Creating a Constructor 
s1=WebDevelpoment() 
 
#Creating Static variables outside the class 
WebDevelpoment.pi=3.14 
 
#Accessing the static variables outside the class 
print(WebDevelpoment.__dict__) 
 
#Fetching the instance Variables: 
print(s1.__dict__) 
 
#calling the instance Method: 
s1.static_variable() 
print(WebDevelpoment.__dict__)