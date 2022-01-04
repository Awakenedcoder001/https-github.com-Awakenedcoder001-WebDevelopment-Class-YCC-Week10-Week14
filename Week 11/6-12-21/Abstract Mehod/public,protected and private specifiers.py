class Pemba: 
 kindness=False 
 _weight=60 
 __height=2.2 
 
 def display(self): 
  print(f"Kindness of Pemba is : {Pemba.kindness}") 
  print(f"Weight of Pemba is : {Pemba._weight}") 
  print(f"Height of Pemba is : {Pemba.__height}") 
 
p=Pemba() 
print(p.kindness) 
p.display() 
 
#Access Protect varibales outside the  class using obj reference 
print(p._weight)  
 
 
#Access Protected varibales outside the  class using class name 
print(Pemba._weight) 
 
#Access Private varibles outside the class: 
print(Pemba.__height) 
print(p.__height)