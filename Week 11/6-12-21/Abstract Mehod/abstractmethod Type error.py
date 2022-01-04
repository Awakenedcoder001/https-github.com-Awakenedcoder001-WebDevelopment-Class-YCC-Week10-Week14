from abc import * 
class Fruits(ABC): 
 def taste(self): 
  print("Most of the fruits are sweet") 
 
 @abstractmethod  
 def season(self): 
  pass 
 
#we cannot create an object of abstract class 
#TypeError: Can't instantiate abstract class Fruits with abstract method season 
obj=Fruits()