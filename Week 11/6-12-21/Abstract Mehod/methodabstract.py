from abc import * 
class Fruits(ABC): 
 def taste(self): 
  print("Most of the fruits are sweet") 
 
 @abstractmethod  
 def season(self): 
  pass 
 
class Mango(Fruits): 
 def season(self): 
  print("Mango is grown in summer season") 
 
obj=Mango() 
obj.season() 
obj.taste()