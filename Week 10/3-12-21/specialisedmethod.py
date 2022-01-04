class Parent: 
 def cooks(self): 
  print("Cooks Gud Food!!") 
 
 def interest(self): 
  print("Parents DOnt know How to Play Online Games") 
 
class Child(Parent): 
 def interest(self): 
  print("Child knows How to Play Online Games") 
  Parent().interest() 
 
 def drinking(self): 
  print("Child Drinks A Lot Of Alcohol And He is Drunkard") 
 
c1=Child() 
c1.cooks() 
c1.interest() 
c1.drinking()