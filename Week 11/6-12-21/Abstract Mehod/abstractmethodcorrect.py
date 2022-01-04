from abc import * 
class Fruits: 
 @abstractmethod 
 def taste(self): 
  print("Most of the fruits are sweet") 
 
 @abstractmethod 
 def season(self): 
  pass 
 
class Mango(Fruits): 
 def season(self): 
  print("Grows in summer season") 
 
obj=Mango() 
obj.taste() 
obj.season()