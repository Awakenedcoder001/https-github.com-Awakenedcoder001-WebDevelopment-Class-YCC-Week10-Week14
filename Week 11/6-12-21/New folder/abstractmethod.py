from abc import * 
class Animal: 
 @abstractmethod 
 def walk(self): 
  pass 
 
 @abstractmethod 
 def eat(self): 
  pass 
 
class Dog(Animal): 
 def walk(self): 
  print("Dog walks") 
 
 @abstractmethod 
 def eat(self): 
  pass 
obj=Dog() 
obj.walk() 
obj.eat() 
Dog.eat(obj)