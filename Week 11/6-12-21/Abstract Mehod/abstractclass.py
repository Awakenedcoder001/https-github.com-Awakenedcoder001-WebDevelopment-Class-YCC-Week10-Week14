from abc import * 
class Fruits(ABC): 
 def taste(self): 
  print("Most of the fruits are sweet") 
 
 @abstractmethod  
 def season(self): 
  pass 
 
class Mango(Fruits): 
 pass 
#sinces mango class is an abstract class we cannot create an object 
obj=Mango()